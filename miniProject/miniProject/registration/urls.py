from django.urls import path
# importing password reset related urls
from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('user-profile/', views.profileView, name='profile'),

    # send users to a page to reset their password
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name='password_reset'),
    # the page shown after a user has been emailed a link to reset their password
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    # presents a form for entering a new password
    path('password_reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    # show users password successfully changed message
    path('password_reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),

]