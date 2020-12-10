from django.urls import path
from .views import Notice2View, SingleNotice2View


app_name = "places"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('places/', Notice2View.as_view()),
    path('places/<int:pk>', SingleNotice2View.as_view()),
]