from django.urls import path
from reviews.apps import ReviewsConfig
from reviews.views import ReviewsListView, ReviewsCreateView, ReviewsDetailView, ReviewsUpdateView, ReviewsDeleteView

app_name = ReviewsConfig.name


urlpatterns = [
    path('', (ReviewsListView.as_view()), name='reviews_list'),
    path('create/', ReviewsCreateView.as_view(), name='reviews_form'),
    path('view/<int:pk>/', ReviewsDetailView.as_view(), name='reviews_detail'),
    path('edit/<int:pk>/', ReviewsUpdateView.as_view(), name='reviews_update_form'),
    path('delete/<int:pk>/', ReviewsDeleteView.as_view(), name='reviews_confirm_delete'),
]