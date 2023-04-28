# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.users import UserViewSet
from .views.client import ClientViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'clients', ClientViewSet, basename='clients')


urlpatterns = [
    path('', include(router.urls)),
]
