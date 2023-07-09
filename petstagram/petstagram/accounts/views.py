from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_view

from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from petstagram.accounts.models import PetstagramUser


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login user')


# def login_user(request):
#     return render(request, 'accounts/login-page.html')


class UserLoginView(auth_view.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('show home page')


class UserLogoutView(auth_view.LogoutView):
    next_page = reverse_lazy('login user')


def details_profile(request, pk):
    return render(request, 'accounts/profile-details-page.html')


# def edit_profile(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')


class UserEditView(views.UpdateView):
    model = PetstagramUser
    template_name = 'accounts/profile-edit-page.html'
    form_class = PetstagramUserEditForm

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.object.pk})


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
