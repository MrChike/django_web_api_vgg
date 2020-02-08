from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('app-viewset', views.AppViewSet, basename='app-viewset')

urlpatterns = [
    path('', include(router.urls))
]
