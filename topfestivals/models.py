from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class Festival(models.Model):
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=120, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zipCode = models.CharField(max_length=120, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    telephone = models.CharField(max_length=120, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="topfestivals", blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('topfestivals:festival_detail', kwargs={'pk': self.pk})

    def averageRating(self):
        reviewCount = self.festivalreview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.festivalreview_set.all()])
            return ratingSum / reviewCount


class Artist(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    age = models.CharField(max_length=120, blank=True, null=True)
    time = models.CharField(max_length=120, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="topfestivals", blank=True, null=True)
    festival = models.ForeignKey(Festival, null=True, related_name='artists', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('topfestivals:artist_detail', kwargs={'pkr': self.festival.pk, 'pk': self.pk})

class Stage(models.Model):
    music = models.TextField(max_length=120, blank=True, null=True)
    description = models.TextField(max_length=120, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    festival = models.ForeignKey(Festival, null=True, related_name='stage', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.music

    def get_absolute_url(self):
        return reverse('topfestivals:stage_detail', kwargs={'pkr': self.festival.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.comment

    def get_absolute_url(self):
        return reverse('topfestivals:review_detail', kwargs={'pkr': self.festival.pk, 'pk': self.pk})


    class Meta:
        abstract = True

class FestivalReview(Review):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("festival", "user")