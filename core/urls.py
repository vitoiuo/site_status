from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('my-sites/', views.sites_list, name = 'sites-list'),
]

