from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('referrals/<str:referral_code>/', views.get_referral_users, name='get_referral_users'),
]