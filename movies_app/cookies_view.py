
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_app.models import Movie
from movies_app.serializers import MovieSerializer


@api_view(['GET'])
def cookies_test(request):

    if request.method == 'GET':
        movies_qs = Movie.objects.all()
    movie_to_exclude = None

    try:
        if request.COOKIES.get('last_viewed_movie_id'):
            movie_to_exclude = int(request.COOKIES.get('last_viewed_movie_id'))

        if movie_to_exclude:
            movies_qs = movies_qs.exclude(pk=movie_to_exclude)
    except Exception as e:
        print("Error")

    serializer = MovieSerializer(movies_qs, many=True)

    response = Response(serializer.data)

    response.set_cookie('last_viewed_movie_id', value=request.COOKIES.get('last_viewed_movie_id'))

    return response

