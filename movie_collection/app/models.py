from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actor = models.ManyToManyField(Actor, related_name="movies", related_query_name="movie")
    release_date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    

def create_owner(name):
    owner = Owner(
        name = name
    )
    owner.save()
    return owner


def create_actor(name, hometown, birthday):
    actor = Actor(
        name = name,
        hometown = hometown,
        birthday = birthday
    )
    actor.save()
    return actor


def create_movie(title, release_date, owner, actors):
    movie = Movie.objects.create(
        title = title,
        release_date = release_date,
        owner = owner
    )
    movie.actor.add(*actors)
    movie.save()
    return movie