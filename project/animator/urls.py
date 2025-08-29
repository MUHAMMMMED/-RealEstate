from django.urls import path, include
from rest_framework import routers
from animator.views import MediaUploadViewSet

router = routers.DefaultRouter()
router.register(r'upload', MediaUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]