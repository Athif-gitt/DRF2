from django.urls import path
from .views import StudentApiView

urlpatterns = [
    path('student/', StudentApiView.as_view(), name='student')
]
