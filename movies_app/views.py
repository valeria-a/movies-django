import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_app.models import Movie


# Create your views here.


@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        response = []
        for m in movies:
            response.append({'name': m.name, 'year': m.release_year})
        # note what to import
        return Response(response)








# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Movies home page")