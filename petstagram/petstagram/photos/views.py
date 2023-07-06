from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as view

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import CreatePhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


class AddPhotoView(view.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = CreatePhotoForm
    # TODO replace success url with correct one
    success_url = reverse_lazy('show home page')


class DetailsPhotoView(view.DetailView):
    template_name = 'photos/photo-details-page.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.get_object()
        likes = photo.like_set.all()
        comments = photo.comment_set.all()

        context.update({
            'photo': photo,
            'likes': likes,
            'comments': comments,
            'comment_form': CommentForm()
        })
        return context


class EditPhotoView(view.UpdateView):
    template_name = 'photos/photo-edit-page.html'
    model = Photo
    form_class = EditPhotoForm
    success_url = reverse_lazy('show home page')


class DeletePhotoView(view.DeleteView):
    model = Photo

    def get(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.delete()
        return redirect(reverse_lazy('show home page'))
