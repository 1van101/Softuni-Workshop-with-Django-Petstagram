from django.urls import path, include

from petstagram.accounts.views import UserRegisterView, UserLoginView, details_profile, delete_profile, \
    UserLogoutView, UserEditView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', details_profile, name='details profile'),
        path('edit/', UserEditView.as_view(), name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)

