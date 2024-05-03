from django.test import TestCase
from app import models as m
from datetime import date

# Create your tests here.
class Test_movie_collection(TestCase):
    def setUp(self):
        self.owner1 = m.create_owner(name="Kelvin")
        self.owner2 = m.create_owner(name="Dustin")
        self.owner3 = m.create_owner(name="Joshua")

        self.actor1 = m.create_actor(name="Leonardo DiCaprio", hometown="Los Angeles, CA", birthday=date(1974, 11, 11))
        self.actor2 = m.create_actor(name="Tim Robbins", hometown="West Covina, CA", birthday=date(1958, 10, 16))
        self.actor3 = m.create_actor(name="Christian Bale", hometown="Haverfordwest, Pembrokeshire, Wales", birthday=date(1974, 1, 30))
        self.actor4 = m.create_actor(name="Tom Hanks", hometown="Concord, CA", birthday=date(1956, 7, 9))
        self.actor5 = m.create_actor(name="Marlon Brando", hometown="Omaha, NE", birthday=date(1924, 4, 3))

        self.movie1 = m.create_movie(title="Inception", actors=[self.actor1, self.actor2], release_date=date(2010, 7, 16), owner=self.owner1)
        self.movie2 = m.create_movie(title="The Shawshank Redemption", actors=[self.actor2], release_date=date(1994, 8, 23), owner=self.owner1)
        self.movie3 = m.create_movie(title="The Dark Knight", actors=[self.actor3], release_date=date(2008, 7, 18), owner=self.owner2)
        self.movie4 = m.create_movie(title="Forrest Gump", actors=[self.actor4], release_date=date(1994, 6, 6), owner=self.owner3)
        self.movie5 = m.create_movie(title="The Godfather", actors=[self.actor5], release_date=date(1972, 3, 24), owner=self.owner2)


    def test_create_owner(self):

        self.assertEqual(self.owner1.name, "Kelvin")
        self.assertEqual(self.owner2.name, "Dustin")
        self.assertEqual(self.owner3.name, "Joshua")


    def test_create_actor(self):

        self.assertEqual(self.actor1.name, "Leonardo DiCaprio")
        self.assertEqual(self.actor2.name, "Tim Robbins")
        self.assertEqual(self.actor3.name, "Christian Bale")
        self.assertEqual(self.actor4.name, "Tom Hanks")
        self.assertEqual(self.actor5.name, "Marlon Brando")

        self.assertEqual(self.actor1.hometown, "Los Angeles, CA")

        self.assertEqual(self.actor1.birthday, date(1974, 11, 11))


    def test_create_movie(self):
    
        self.assertEqual(self.movie1.title, "Inception")
        self.assertEqual(self.movie1.owner, self.owner1)
        self.assertEqual(self.movie1.release_date, date(2010, 7, 16))
        self.assertIn(self.actor1, self.movie1.actor.all())
        self.assertIn(self.actor2, self.movie1.actor.all())
