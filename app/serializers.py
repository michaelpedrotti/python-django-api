from rest_framework import serializers
from app.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        # fields = ['id', 'name']