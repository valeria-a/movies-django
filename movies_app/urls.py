from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views, cookies_view
from .movies_viewset import MoviesViewSet

# automatically defining urls for MoviesViewSet
router = DefaultRouter()
router.register(r'api/movies', MoviesViewSet, basename='movie')


urlpatterns = [

    path('', views.index),
    path('browser_storage', views.browser_storage),
    path('api/cookies_test', cookies_view.cookies_test)


    # path('api/movies', views.movies_list),
    # path('api/movies/<int:movie_id>', views.movie_details),
    # path('api/movies/<int:movie_id>/actors', views.movie_actors)
]

# adding movies urls to urlpatterns
urlpatterns.extend(router.urls)
