from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomEditUserForm, NewCustomEditUserForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class UserCreateProfileView(CreateView):
    model = User
    form_class = NewCustomEditUserForm
    template_name = 'users/user_create.html'
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.set_password(form.data.get('password'))
            self.object.save()
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('prod:product')

    def get_object(self, queryset=None):
        return self.request.user