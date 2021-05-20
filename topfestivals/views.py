from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from topfestivals.models import FestivalReview, Festival, Artist, Review
from topfestivals.forms import FestivalForm, ArtistForm, ReviewForm

# Security Mixins

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'topfestivals/form.html'

# HTML Views

class FestivalDetail(DetailView):
    model = Festival
    template_name = 'topfestivals/festival_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FestivalDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = FestivalReview.RATING_CHOICES
        return context


class FestivalCreate(LoginRequiredMixin, CreateView):
    model = Festival
    template_name = 'topfestivals/form.html'
    form_class = FestivalForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FestivalCreate, self).form_valid(form)


class FestivalDelete(LoginRequiredMixin, DeleteView):
    model = Festival
    success_url = reverse_lazy('home')
    template_name = 'topfestivals/festival_delete.html'

    def test_func(self):
        festival = Festival.objects.filter(pk=self.kwargs['pk']).first()
        return festival is not None and self.request.user.pk == festival.user.pk


class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    template_name = 'topfestivals/form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.festival = Festival.objects.get(id=self.kwargs['pk'])
        return super(ArtistCreate, self).form_valid(form)


class ArtistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    success_url = reverse_lazy('home')
    template_name = 'topfestivals/artist_delete.html'

    def test_func(self):
        artist = Artist.objects.filter(pk=self.kwargs['pk']).first()
        return artist is not None and self.request.user.pk == artist.user.pk


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('home')
    template_name = 'topfestivals/review_delete.html'

    def test_func(self):
        review = Review.objects.filter(pk=self.kwargs['pk']).first()
        return review is not None and self.request.user.pk == review.user.pk



@login_required()
def review(request, pk):
    festival = get_object_or_404(Festival, pk=pk)
    if FestivalReview.objects.filter(festival=festival, user=request.user).exists():
        FestivalReview.objects.get(festival=festival, user=request.user).delete()
    new_review = FestivalReview(
        rating=request.POST.get('rating', 0),
        comment=request.POST['comment'],
        user=request.user,
        festival=festival)
    new_review.save()
    return HttpResponseRedirect(reverse('topfestivals:festival_detail', args=(festival.id,)))

