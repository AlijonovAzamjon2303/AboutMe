from tkinter.font import names

from django.urls import path

from config.urls import urlpatterns
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
