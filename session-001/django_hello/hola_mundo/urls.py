from django.urls import path

from . import views

urlpatterns = [
    # path del index
    path("", views.index, name="index"),
]