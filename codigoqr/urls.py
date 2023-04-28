# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import qr as qrViews
from .views import coordenate as coordenateView

router = DefaultRouter()

router.register(r'code', qrViews.CodeQrView, basename='qr')
router.register(r'coordenadas',
                coordenateView.CoordenateView, basename='coordenadas')

urlpatterns = [
    path('', include(router.urls)),
]
