from django.db import models

class Owner(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.fname + ' ' + self.lname


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
    

def create_owner(fname, lname):
    owner = Owner(
        fname = fname,
        lname = lname
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


def create_movie(title, actor, release_date, owner):
    movie_name = Movie(
        title = title,
        actor = actor,
        release_date = release_date,
        owner = owner
    )
    movie_name.save()
    return movie_name