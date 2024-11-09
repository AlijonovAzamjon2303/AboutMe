from django.urls import path
from .views import HomePageView, name_view, data_view
from . import views

urlpatterns = [
    path('data/', views.data_view, name='data'),
    path('', HomePageView.as_view(), name='home'),
    path('save-name/', views.name_view, name='save_name'),
]
