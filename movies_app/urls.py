from django.urls import path

from . import views

urlpatterns = [
    path('api/movies', views.movies_list)
    # path('', views.index, name='index'),
]