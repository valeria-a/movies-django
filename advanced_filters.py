import datetime
import os

from django.db.models import Avg, Min, Max, Count

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

import django
django.setup()

from movies_app.models import *


#https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups
def filter_movies():
    query_set = Movie.objects.filter(id=7)
    print(query_set)
    movie_obj = Movie.objects.get(id=7)
    print(movie_obj)

    qs = Movie.objects.filter(duration_in_min__gt=150)
    print(qs)

    qs = Movie.objects.filter(name__icontains='the')
    print(qs)

    qs = Movie.objects.filter(name__icontains='the', pic_url__isnull=False)
    print(qs)


def relationships():
    qs = Movie.objects.filter(movieactor__salary__gt=4000000)
    print(qs)

    qs = Movie.objects.filter(actors__birth_year__lt=1970)
    print(qs)


# https://docs.djangoproject.com/en/4.1/topics/db/queries/#querysets-are-lazy
def chaining_querysets():
    pass


# https://docs.djangoproject.com/en/4.1/topics/db/aggregation/
def aggregation():
    # count all movies
    # ret_val = Movie.objects.all().count()

    # avg duration across all movies
    ret_val = Movie.objects.aggregate(
        Avg('duration_in_min'), Min('duration_in_min'), Max('duration_in_min'))
    print(ret_val)


#https://docs.djangoproject.com/en/4.1/topics/db/aggregation/
def annotation():
    # Generating aggregates for each item in a QuerySet

    # option 1
    # ret_val = Movie.objects.annotate(Count('actors'))
    # for r in ret_val:
    #     print(r, r.actors__count)

    # option 2
    ret_val = Movie.objects.annotate(actors_count=Count('actors'))
    for r in ret_val:
        print(r, r.actors_count)

def annotation2():
    # ret_val = Movie.objects.annotate(
    #     youngest_actor=Max('actors__birth_year'),
    #     oldest_actor=Min('actors__birth_year'))

    ret_val = Movie.objects.annotate(
        youngest_actor=datetime.date.today().year - Max('actors__birth_year'),
        oldest_actor=datetime.date.today().year - Min('actors__birth_year'))

    for r in ret_val:
        print(r, r.youngest_actor, r.oldest_actor)


def group_by():
    # group movies by year and count
    ret_val = Movie.objects.values('release_year').annotate(movies_per_year=Count('id'))
    print(ret_val)


def or_queries():
    pass


# https://docs.djangoproject.com/en/4.2/topics/db/sql/#performing-raw-sql-queries
def raw_query():
    pass



if __name__ == '__main__':
    # aggregation()
    # filter_movies()
    # relationships()
    # annotation()
    # annotation2()
    # m = Movie.objects.get(id=3)
    # print(Movie.objects.filter(movieactor__salary__gt=2000000))
    group_by()