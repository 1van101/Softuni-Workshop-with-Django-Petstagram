from django.urls import path, include

from petstagram.photos.views import AddPhotoView, DetailsPhotoView, EditPhotoView, DeletePhotoView

urlpatterns = (
    path('add/', AddPhotoView.as_view(), name='add photo'),
    path('<int:pk>/', include([
        path('', DetailsPhotoView.as_view(), name='details photo'),
        path('edit/', EditPhotoView.as_view(), name='edit photo'),
        path('delete/', DeletePhotoView.as_view(), name='delete photo')
    ])),

)
