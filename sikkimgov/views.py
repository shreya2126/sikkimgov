from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import beneficiaries as beneficiaries2
from .serializers import beneficiariesSerializer 

class beneficiaries(APIView):
    def get(self, request):
        beneficiaries1=beneficiaries2.objects.all()
        serializer=beneficiariesSerializer(beneficiaries1, many=True)
        return Response(serializer.data)

    def post(self):  
        pass


