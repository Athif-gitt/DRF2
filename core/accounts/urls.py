from django.urls import path, include
from .views import RegisterApi, LoginApi, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename="books")

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', LoginApi.as_view()),
    path('', include(router.urls)),
]