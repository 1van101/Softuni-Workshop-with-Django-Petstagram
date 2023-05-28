from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('profile/<int:pk>/', include([
        path('', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)