from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from reviews.forms import VersionForm
from reviews.forms import ReviewForm
from reviews.models import Review, Version


class ReviewsListView(ListView):
    model = Review
    extra_context = {
        'title': 'Отзывы'
    }
    template_name = 'reviews/reviews_list.html'


class ReviewsCreateView(CreateView):
    model = Review
    permission_required = 'reviews.create_review'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:reviews_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Review, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ReviewsUpdateView(UpdateView):
    model = Review
    permission_required = 'reviews.change_review'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:reviews_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Review, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ReviewsDeleteView(DeleteView):
    model = Review
    permission_required = 'reviews.delete_review'
    success_url = reverse_lazy('reviews:reviews_list')


class ReviewsDetailView(DetailView):
    model = Review
    permission_required = 'reviews.detail_review'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:reviews_list')

