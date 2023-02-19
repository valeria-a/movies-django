import datetime

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from movies_app.models import Movie
from movies_app.serializers import MovieSerializer, MovieOverviewSerializer, MovieActorSerializer


# class MoviesViewSet(viewsets.ModelViewSet):
#     pass

# class MoviesViewSet(mixins.ListModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     viewsets.GenericViewSet):
#
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MoviesViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()

    # we need different serializers for different actions
    # serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieOverviewSerializer
        else:
            return MovieSerializer

    def list(self, request, *args, **kwargs):
        print(f"Cookies received: {request.COOKIES}")
        response = super().list(request, *args, **kwargs)
        return response

    def get_queryset(self):

        movies_qs = self.queryset
        if self.action == 'list':
            if 'name' in self.request.query_params:
                movies_qs = movies_qs.filter(name__iexact=self.request.query_params['name'])
            if 'duration_from' in self.request.query_params:
                movies_qs = movies_qs.filter(duration_in_min__gte=self.request.query_params['duration_from'])
            if 'duration_to' in self.request.query_params:
                movies_qs = movies_qs.filter(duration_in_min__lte=self.request.query_params['duration_to'])
            if 'description' in self.request.query_params:
                movies_qs = movies_qs.filter(description__icontains=self.request.query_params['description'])

            movie_to_exclude = None
            try:
                if self.request.COOKIES.get('last_viewed_movie_id'):
                    movie_to_exclude = int(self.request.COOKIES.get('last_viewed_movie_id'))

                if movie_to_exclude:
                    movies_qs = movies_qs.exclude(pk=movie_to_exclude)
            except Exception as e:
                print("Error")

        return movies_qs

    @action(methods=['GET'], detail=True, url_path='actors')
    def movie_actors(self, request, pk=None):

        # note usage of get_object
        movie = self.get_object()
        serializer = MovieActorSerializer(movie.movieactor_set, many=True)
        return Response(serializer.data)



