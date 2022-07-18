from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('my-sites/', views.sites_list, name = 'sites-list'),
    path('site-view/<int:id>', views.view_site, name='view-site'),
    path('add-site/', views.add_site, name='add-site'),
    path('edit-site/<int:id>', views.edit_site, name='edit-site'),
    path('delete-site/<int:id>', views.delete_site, name='delete-site'),

]

