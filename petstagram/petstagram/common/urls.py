from django.urls import path

from petstagram.common.views import home_page, like_functionality, share_functionality, AddCommentView

urlpatterns = (
    path('', home_page, name='show home page'),
    path('like/<int:photo_id>/', like_functionality, name='like functionality'),
    path('share/<int:photo_id>/', share_functionality, name='share functionality'),
    path('comment/<int:photo_id>/', AddCommentView.as_view(), name='add comment')
)