from django.urls import path, include
from app.urls import urls

urlpatterns = [
    path('', include(urls())),
]
