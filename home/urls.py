from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup2/', views.Signup.as_view(), name='signup2'),
    path('game/', views.game.as_view(), name='game'),
]