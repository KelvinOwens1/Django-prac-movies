from django.test import TestCase
from app import models as m
from datetime import date

# Create your tests here.
class Test_movie_collection(TestCase):
    def setUp(self):
        self.owner1 = m.create_owner(fname="Kelvin", lname="Owens")
        self.owner2 = m.create_owner(fname="Dustin", lname="Weeks")
        self.owner3 = m.create_owner(fname="Joshua", lname="Mooneyham")

        self.actor1 = m.create_actor(name="Leonardo DiCaprio", hometown="Los Angeles, CA", birthday=date(1974, 11, 11))
        self.actor2 = m.create_actor(name="Tim Robbins", hometown="West Covina, CA", birthday=date(1958, 10, 16))
        self.actor3 = m.create_actor(name="Christian Bale", hometown="Haverfordwest, Pembrokeshire, Wales", birthday=date(1974, 1, 30))
        self.actor4 = m.create_actor(name="Tom Hanks", hometown="Concord, CA", birthday=date(1956, 7, 9))
        self.actor5 = m.create_actor(name="Marlon Brando", hometown="Omaha, NE", birthday=date(1924, 4, 3))

        self.movie1 = m.create_movie(title="Inception", actor=self.actor1, release_date=date(2010, 7, 16), owner=self.owner1)
        self.movie2 = m.create_movie(title="The Shawshank Redemption", actor=self.actor2, release_date=date(1994, 8, 23), owner=self.owner1)
        self.movie3 = m.create_movie(title="The Dark Knight", actor=self.actor3, release_date=date(2008, 7, 18), owner=self.owner2)
        self.movie4 = m.create_movie(title="Forrest Gump", actor=self.actor4, release_date=date(1994, 6, 6), owner=self.owner3)
        self.movie5 = m.create_movie(title="The Godfather", actor=self.actor4, release_date=date(1972, 3, 24), owner=self.owner2)


    def test_create_owner(self):

        self.assertEqual(self.owner1.fname, "Kelvin")
        self.assertEqual(self.owner2.fname, "Dustin")
        self.assertEqual(self.owner3.fname, "Joshua")
