from django.urls import path
from .views import NoticeView


app_name = "places"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('places/', NoticeView.as_view()),
    path('places/<int:pk>', NoticeView.as_view())
]