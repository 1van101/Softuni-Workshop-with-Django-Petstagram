from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import views as auth_view
from django.contrib.auth import get_user_model

from petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_view.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('show home page')


class UserLogoutView(auth_view.LogoutView):
    next_page = reverse_lazy('login user')

@method_decorator(login_required, name='dispatch')
class UserDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())
        is_owner = self.request.user == self.object
        context.update({
            'total_likes_count': total_likes_count,
            'is_owner': is_owner
        })

        return context

@method_decorator(login_required, name='dispatch')
class UserEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit-page.html'
    form_class = PetstagramUserEditForm

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class UserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('show home page')
