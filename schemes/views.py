from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable,NotAuthenticated, NotFound,PermissionDenied
from . import models,serializers

# Create your views here.


#get schemes
class SchemeView(generics.ListAPIView):
    def get_serializer_class(self):
        idd = self.request.GET.get('id')
        if idd:
            return serializers.SchemeSerializer
        else:
            return serializers.LandingSchemeSerializer

    def get_queryset(self):
        idd = self.request.GET.get('id')
        if idd:
            return models.Schemes.objects.filter(id=idd)
        else:
            queryset = models.Schemes.objects.all()
            return queryset