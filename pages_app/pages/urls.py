from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),  # Corrected path with a trailing slash
    path('', HomePageView.as_view(), name='home'),
]