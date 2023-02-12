import json

from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_app.models import *
from movies_app.serializers import *


# Create your views here.


# Example of simple request without serializers
# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         response = []
#         for m in movies:
#             response.append({'name': m.name, 'year': m.release_year})
#         # note what to import
#         return Response(response)

# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def movies_list(request):

    if request.method == 'GET':
        movies_qs = Movie.objects.all()

        if 'name' in request.query_params:
            movies_qs = movies_qs.filter(name__iexact=request.query_params['name'])
        if 'duration_from' in request.query_params:
            movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
        if 'duration_to' in request.query_params:
            movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
        if 'description' in request.query_params:
            movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

        serializer = MovieSerializer(movies_qs, many=True)
        if not serializer.data:
            return Response(data=[], status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            new_movie = serializer.create(serializer.validated_data)
            # if we want to return the created object
            return Response(data=MovieSerializer(new_movie, many=False).data)


@api_view(['GET', 'PATCH', 'DELETE'])
def movie_details(request, movie_id):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data)
        # follow-up: how can i check which exception is thrown?
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PATCH':
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie, data=request.data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()
    elif request.method == 'DELETE':
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return Response()


@api_view(['GET', 'POST'])
def movie_actors(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieActorSerializer(movie.movieactor_set, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddMovieActorSerializer(data=request.data, many=False, context={'movie_id': movie_id, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response()


def index(request):
    # return render(request, "static/imdb.html")
    return render(request, "static/index.html")

def browser_storage(request):
    return render(request, "browser_storage.html")