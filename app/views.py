from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ProfileModel
from .serializers import ProfileSerializer
import sys


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer

    def list(self, req):
        res =  super().list(self, req)

        # print(res.data, file=sys.stderr)

        res.data = { "error": False, "rows": res.data }
        return res