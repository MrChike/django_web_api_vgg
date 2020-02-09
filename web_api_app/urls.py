from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('users/register', views.UsersProfileViewSet)
router.register('projects', views.ProjectsViewSet)

urlpatterns = [
    path('users/auth', views.UsersAuthApiView.as_view()),
    path('', include(router.urls)),
]
