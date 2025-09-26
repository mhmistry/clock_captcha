from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signed-in/', views.signed_in, name='signed_in'),
]
