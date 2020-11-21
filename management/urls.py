from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('register/', views.registerPage, name="register"),
    path('dashboard', views.home, name='home'),
    path('delete/<str:qid>', views.delete_emp, name="delete_emp"),
    path('edit/<str:qid>', views.edit_emp, name="edit_emp"),
    path('profile', views.managerProfile, name='profile'),
]
