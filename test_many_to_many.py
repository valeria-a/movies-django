import os

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

import django
django.setup()

from movies_app.models import *

def create_data():
    m = Movie.objects.get(id=1)

    a1 = Actor.objects.create(name='David Craig', birth_year=1968)

    # a2 = Actor(name="Edward Norton", birth_year=1969)
    # a2.save()

    MovieActor.objects.create(movie=m, actor=a1, main_role=True, salary=1_300_000)


def create_data2():
    m = Movie.objects.get(id=1)
    m.actors.create(name="Edward Norton", birth_year=1969, through_defaults={
        'main_role': False,
        'salary': 500_000
    })
    m.save()


def query_data_demo():
    m = Movie.objects.get(id=1)
    print(m)
    print(m.actors.all())
    print(m.movieactor_set.all())

    a = Actor.objects.filter(name='David Craig').all()[0]
    print(a)
    print(a.movie_set.all())
    print(a.movieactor_set.all())


def update_data_demo():
    ma = MovieActor.objects.filter(movie_id=1, actor_id=1).all()[0]
    print(ma)
    ma.salary = 2_000_000
    ma.save()


if __name__ == '__main__':
    # create_data()
    create_data2()
    # query_data_demo()
    # update_data_demo()


