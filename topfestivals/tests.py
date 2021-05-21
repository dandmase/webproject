from django.contrib.auth.models import User
from django.test import TestCase

from .models import Festival, FestivalReview, Artist


class FestivalReviewTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        trendy = Festival.objects.create(name="Trendy Festival", user=user1)
        fullfest = Festival.objects.create(name="Full Festival", street="Route 66", city="Arkansas", country="United States", user=user2)
        FestivalReview.objects.create(rating=3, comment="Average...", festival=trendy, user=user1)
        FestivalReview.objects.create(rating=5, comment="Excellent!", festival=trendy, user=user2)
        FestivalReview.objects.create(rating=5, comment="Very Nice!", festival=fullfest, user=user2)
        FestivalReview.objects.create(rating=1, comment="Really bad!", festival=trendy, user=user3)
        Festival.objects.create(name="Unknown Festival", user=user1)
        Artist.objects.create(name="Lady Gaga", festival=fullfest, user=user3)
        Artist.objects.create(name="Els Catarres", festival=fullfest, user=user2)
        Artist.objects.create(name="Celine Dion", festival=fullfest, user=user2)

    def test_average_3reviews(self):
        """The average review for a trendy festival with 3 reviews is properly computed"""
        festival = Festival.objects.get(name="Trendy Festival")
        self.assertEqual(festival.averageRating(), 3)

    def test_average_3artist(self):
        """The average review for a full festival with 3 artist is properly computed"""
        festival = Festival.objects.get(name="Full Festival")
        self.assertEqual(festival.artists.count(), 3)


    def test_average_no_review(self):
        """The average review for a festival without reviews is 0"""
        festival = Festival.objects.get(name="Unknown Festival")
        self.assertEqual(festival.averageRating(), 0)