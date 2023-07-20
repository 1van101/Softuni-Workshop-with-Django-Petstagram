from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as view

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


@method_decorator(login_required, name='dispatch')
class AddPhotoView(view.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = CreatePhotoForm
    # TODO replace success url with correct one
    success_url = reverse_lazy('show home page')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DetailsPhotoView(view.DetailView):
    template_name = 'photos/photo-details-page.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.get_object()
        likes = photo.like_set.all()
        comments = photo.comment_set.all()
        photo_is_liked_by_user = likes.filter(user=self.request.user)

        context.update({
            'photo': photo,
            'likes': likes,
            'comments': comments,
            'comment_form': CommentForm(),
            'photo_is_liked_by_user': photo_is_liked_by_user
        })
        return context

@method_decorator(login_required, name='dispatch')
class EditPhotoView(view.UpdateView):
    template_name = 'photos/photo-edit-page.html'
    model = Photo
    form_class = EditPhotoForm
    success_url = reverse_lazy('show home page')

@method_decorator(login_required, name='dispatch')
class DeletePhotoView(view.DeleteView):
    model = Photo

    def get(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.delete()
        return redirect(reverse_lazy('show home page'))
