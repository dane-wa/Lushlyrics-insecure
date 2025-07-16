from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),
    path("register/", views.register, name='register'),
    path("login/", views.loginView, name='login'),
    path("logout/", views.logoutView, name='logout'),

    # création de lien de récupération de mots de passe
    path('mot-de-passe-oublie/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('mot-de-passe-envoye/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reinitialiser/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('mot-de-passe-reinitialise/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
