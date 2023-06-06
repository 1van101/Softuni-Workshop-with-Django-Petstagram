from pyperclip import copy
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def index(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_obj = Like.objects.filter(to_photo_id=photo_id)

    if liked_obj:
        liked_obj.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })

    copy(request.META['HTTP_HOST'] + photo_details_url)

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
