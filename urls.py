from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_of_the_day, name='word_of_the_day'),
]
