from rest_framework import serializers
from . import models


class SchemeSerializer(serializers.ModelSerializer):
    Pic = serializers.ImageField
    class Meta:
        model = models.Schemes
        fields = "__all__"



class LandingSchemeSerializer(serializers.ModelSerializer):
    Pic = serializers.ImageField
    class Meta:
        model = models.Schemes
        fields = ['id','Title','Description','Pic']