from django.urls import path, include

from petstagram.accounts.views import UserRegisterView, UserLoginView, UserDetailsView, UserDeleteView, \
    UserLogoutView, UserEditView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details profile'),
        path('edit/', UserEditView.as_view(), name='edit profile'),
        path('delete/', UserDeleteView.as_view(), name='delete profile'),
    ]))
)

