from django.urls import path
from reviews.apps import ReviewsConfig
from reviews.views import review

app_name = ReviewsConfig.name


urlpatterns = [
    path('', review, name='review')
]