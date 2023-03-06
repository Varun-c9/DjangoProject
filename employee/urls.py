from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('user_detail/', views.user_detail_view, name='user_detail'),
    path('edit_user/<int:user_id>/', views.edit_user_view, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user_view, name='delete_user'),
    path('logout/', views.logout_view, name='logout'),
]
