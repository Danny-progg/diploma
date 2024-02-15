from django.shortcuts import render
from reviews.models import Review


def review(request):
    context = {
        'object_list': Review.objects.all(),
        'title': 'Отзывы'
    }
    return render(request, 'reviews/review_list.html', context)
