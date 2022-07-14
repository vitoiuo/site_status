from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=forms.LoginForm,
        ),
        name="login",
    ),
    path('register/', views.SignUp.as_view(), name='signup'),
    #path('logout/', auth_views.LoginView.as_view(), name='logout')
]