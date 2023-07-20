from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as view

from petstagram.accounts.models import PetstagramUser
from petstagram.common.forms import CommentForm
from petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet


@method_decorator(login_required, name='dispatch')
class AddPetView(view.CreateView):
    template_name = 'pets/pet-add-page.html'
    form_class = AddPetForm
    success_url = reverse_lazy('show home page')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditPetView(view.UpdateView):
    template_name = 'pets/pet-edit-page.html'
    model = Pet
    form_class = EditPetForm
    success_url = reverse_lazy('show home page')


@method_decorator(login_required, name='dispatch')
class DeletePetView(view.DeleteView):
    template_name = 'pets/pet-delete-page.html'
    model = Pet
    form_class = DeletePetForm
    success_url = reverse_lazy('show home page')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs


@method_decorator(login_required, name='dispatch')
class DetailsPetView(view.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        all_liked_photos_by_request_user = [like.to_photo_id for like in
                                            self.object.user.like_set.all()] if self.object.user.is_authenticated else []
        photos = pet.photo_set.all()
        comment_form = CommentForm()
        owner = PetstagramUser.objects.get(username=pet.user.username)

        context.update({
            'photos': photos,
            'owner': owner,
            'all_liked_photos_by_request_user': all_liked_photos_by_request_user,
            'comment_form': comment_form
        })

        return context
