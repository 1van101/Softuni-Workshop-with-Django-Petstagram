from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet


class AddPetView(view.CreateView):
    template_name = 'pets/pet-add-page.html'
    form_class = AddPetForm
    # TODO: change success url with correct one
    success_url = reverse_lazy('show home page')


class EditPetView(view.UpdateView):
    template_name = 'pets/pet-edit-page.html'
    model = Pet
    form_class = EditPetForm
    success_url = reverse_lazy('show home page')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('pet_slug')
        queryset = self.get_queryset()
        obj = queryset.filter(slug=slug).first()
        return obj


class DeletePetView(view.DeleteView):
    template_name = 'pets/pet-delete-page.html'
    model = Pet
    form_class = DeletePetForm
    success_url = reverse_lazy('show home page')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('pet_slug')
        queryset = self.get_queryset()
        obj = queryset.filter(slug=slug).first()
        return obj

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs
# def details_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     print(pet)
#     all_photos = pet.photo_set.all()
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#
#     }
#     return render(request, 'pets/pet-details-page.html', context=context)

class DetailsPetView(view.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        all_photos = pet.photo_set.all()
        context['all_photos'] = all_photos
        return context


