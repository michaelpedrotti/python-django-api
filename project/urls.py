from django.contrib import admin
from django.urls import path, include
from app.views import ProfileViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename="Profile")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
