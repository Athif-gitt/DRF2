from django.urls import path
from .views import ExternalApiView

urlpatterns = [
    path('fetch/', ExternalApiView.as_view())
]
