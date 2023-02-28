from rest_framework import routers
from .views import ProfileViewSet

def urls():
    router = routers.DefaultRouter()
    router.register('profile', ProfileViewSet)
    # router.register('user', UserViewSet, basename="User")
    return router.urls
    