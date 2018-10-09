from django.urls import path
from . import views


urlpatterns = [
    path('', views.time_app, name='time_app'),

]