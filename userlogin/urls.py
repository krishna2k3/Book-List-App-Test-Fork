from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path("profile", views.view_profile, name="profile"),
]