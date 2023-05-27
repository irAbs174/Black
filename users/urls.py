'''
Accounts urls configuration
'''

# Import all requirements
from django.urls import path
from allauth.account.views import LoginView, SignupView, LogoutView, PasswordSetView, PasswordChangeView, PasswordResetView, ConnectionsView
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('set_password/', PasswordSetView.as_view(), name='set_password'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('rest_password/', PasswordResetView.as_view(), name='rest_password'),
    path('social/', ConnectionsView.as_view(), name='social'),
]
