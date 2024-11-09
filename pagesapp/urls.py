from django.urls import path
from .views import HomePageView, name_view
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('save-name/', views.name_view, name='save_name'),
]
