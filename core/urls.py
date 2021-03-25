from django.urls import path
from core import views

urlpatterns = [
    path('access', views.Access.as_view(), name='access'),
    path('', views.home, name='home'),
    path('logout', views.logout_view, name='logout')
]
