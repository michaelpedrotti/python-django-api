from rest_framework import viewsets
from app.models import ProfileModel
from app.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer