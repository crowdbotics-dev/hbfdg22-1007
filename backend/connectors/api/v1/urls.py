from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UiconnectorViewSet

router = DefaultRouter()
router.register("uiconnector", UiconnectorViewSet, basename="uiconnector")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
