from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView, DeleteView
from topfestivals.models import Festival, Artist, Review
from topfestivals.forms import FestivalForm, ArtistForm, ReviewForm
from topfestivals.views import FestivalCreate, FestivalDelete, ArtistDelete, ReviewDelete, ArtistCreate, FestivalDetail, review, LoginRequiredCheckIsOwnerUpdateView
from . import views

app_name = "topfestivals"

urlpatterns = [
    # List latest 5 festivals: /topfestivals/
    path('',
         ListView.as_view(
             queryset=Festival.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
             context_object_name='latest_festival_list',
             template_name='topfestivals/festival_list.html'),
         name='festival_list'),

    # Festival details, ex.: /topfestivals/festivals/1/
    path('festivals/<int:pk>',
         FestivalDetail.as_view(),
         name='festival_detail'),

    # Festival artist details, ex: /topfestivals/festivals/1/artists/1/
    path('festivals/<int:pkr>/artists/<int:pk>',
         DetailView.as_view(
             model=Artist,
             template_name='topfestivals/artist_detail.html'),
         name='artist_detail'),

    # Create a festival, /topfestivals/festivals/create/
    path('festivals/create',
         FestivalCreate.as_view(),
         name='festival_create'),

    # Create a festival artist, ex.: /topfestivals/festivals/1/artists/create/
    path('festivals/<int:pk>/artists/create',
         ArtistCreate.as_view(),
         name='artist_create'),

    # Edit festival details, ex.: /topfestivals/festivals/1/edit/
    path('festivals/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Festival,
             form_class=FestivalForm),
         name='festival_edit'),

    # Edit festival artist details, ex.: /topfestivals/festivals/1/artists/1/edit/
    path('festivals/<int:pkr>/artists/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Artist,
             form_class=ArtistForm),
         name='artist_edit'),

    # Create a festival review, ex.: /topfestivals/festivals/1/reviews/create/
    path('festivals/<int:pk>/reviews/create',
         review,
         name='review_create'),

    # Delete festival details, ex.: /topfestivals/festivals/delete/
    path('festival/delete/<int:pk>', views.FestivalDelete.as_view(),
         name='festival_delete'),

    # Delete artist details, ex.: /topfestivals/artist/delete/
    path('artist/delete/<int:pk>', views.ArtistDelete.as_view(),
         name='artist_delete'),

    # Delete review details, ex.: /topfestivals/review/delete/
    path('review/delete/<int:pk>', views.ReviewDelete.as_view(),
         name='review_delete'),

    # Edit festival review details, ex.: /topfestivals/festivals/1/review/1/edit/
    path('festivals/<int:pkr>/review/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Review,
             form_class=ReviewForm),
         name='review_edit'),

]