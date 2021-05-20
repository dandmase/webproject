from django.forms import ModelForm
from topfestivals.models import Festival, Artist, Review

class FestivalForm(ModelForm):
    class Meta:
        model = Festival
        exclude = ('user', 'date',)

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user', 'date', 'festival',)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'date', 'festival',)
