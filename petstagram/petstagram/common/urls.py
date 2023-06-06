from django.urls import path

from petstagram.common.views import index, like_functionality, share_functionality

urlpatterns = (
    path('', index, name='show home page'),
    path('like/<int:photo_id>/', like_functionality, name='like functionality'),
    path('share/<int:photo_id>/', share_functionality, name='share functionality')

)