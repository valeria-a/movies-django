import os

from django.db.models import Min, Max, Count

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

import django
django.setup()

from movies_app.models import Movie, Rating, Actor

# new_movie = Movie(
#     name='Glass Onion',
#     description="Famed Southern detective Benoit Blanc travels to Greece for his latest case.",
#     duration_in_min=139,
#     release_year=2022,
#     pic_url="https://upload.wikimedia.org/wikipedia/en/6/62/Glass_Onion_poster.jpg"
# )
#
# new_movie.save()


# movies = Movie.objects.all()
# for movie in movies:
#     print(movie.description)
#     print(movie.duration_in_min)
    # new_rating = Rating(movie=movie, rating=9)
    # new_rating.save()

# all_actors = Actor.objects.annotate(min_rating=Min('movie__rating__rating'), max_rating=Max('movie__rating__rating'))
# for a in all_actors:
#     print(a.name, a.min_rating, a.max_rating)

# all_actors = Actor.objects.annotate(Count('movie'))