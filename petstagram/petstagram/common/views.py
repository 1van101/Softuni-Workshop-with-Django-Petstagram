from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pyperclip import copy
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic as view
from django import forms

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    user = request.user
    all_liked_photos_by_request_user = [like.to_photo_id for like in
                                        user.like_set.all()] if user.is_authenticated else []

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            pet_name = search_form.cleaned_data['pet_name']
            all_photos = all_photos.filter(tagged_pets__name__icontains=pet_name).all()

    context = {
        'photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_liked_photos_by_request_user': all_liked_photos_by_request_user
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_obj = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_obj:
        liked_obj.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })

    copy(request.META['HTTP_HOST'] + photo_details_url)

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


@method_decorator(login_required, name='dispatch')
class AddCommentView(view.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        photo_id = self.kwargs['photo_id']
        photo = Photo.objects.get(id=photo_id)

        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.user = self.request.user
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        photo_id = self.kwargs['photo_id']
        return f'{self.request.META["HTTP_REFERER"]}#{photo_id}'
