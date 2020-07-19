from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import beneficiaries
from .models import Intermediatorloginform
from .models import UserLogin
from .models import intermediatorLogin
from django.views.decorators.csrf import csrf_exempt
from .serializers import beneficiariesSerializer 
from .serializers import IntermediatorloginformSerializer,intermediatorLoginSerializer,UserLoginSerializer
from datetime import datetime
import json
from . import models
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from . import models,serializers
from rest_framework import generics


@csrf_exempt
def signup(request):
    content = json.loads(request.body.decode('utf-8'))
    print ('dasdasd  =>  ', content)
    emp = employees.objects.create(
        firstname = content['firstname'],
        lastname = content['lastname'],
        password = content['password'],
    )
    return HttpResponse(json.dumps(content), content_type='application/json', status=200) 

    
    
class beneficiaries(APIView):
    def get(self,request):
        beneficiaries = models.beneficiaries.objects.all()
        serializer=beneficiariesSerializer(beneficiaries, many=True)
        return Response(serializer.data)

    def post(self,request):
        beneficiaries = models.beneficiaries.objects.all()
        serializer=beneficiariesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    def put(self,request):
        beneficiaries = models.beneficiaries.objects.all()
        serializer=beneficiariesSerializer(beneficiaries, many=True)
        return Response(serializer.data)



class intermediatorloginform(APIView):
    def get(self,request):
        intermediatorloginform=Intermediatorloginform.objects.all()
        serializer=IntermediatorloginformSerializer(intermediatorloginform, many=True)
        return Response(serializer.data)

    def post(self,request):
        intermediatorloginform=Intermediatorloginform.objects.all()
        serializer=IntermediatorloginformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data)

    def put(self,request):
        intermediatorloginform=Intermediatorloginform.objects.all()
        serializer=IntermediatorloginformSerializer(intermediatorloginform, many=True)
        return Response(serializer.data)



class UserLogin(generics.GenericAPIView):
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
    serializer_class = serializers.UserLoginSerializer
    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({"Error": "Please provide username/password"}, status="400")
        idd = request.data['userid']
        password = request.data['password']
        try:
            user = models.UserLogin.objects.get(userid=idd, password=password)
        except:
                return Response({"Error": "Invalid username/password"}, status="400")
        if user:
            jwt_token = self.get_tokens_for_user(user)
            payload = jwt.decode(jwt_token['access'], 'SECRET_KEY')
            return Response({
                "access" : jwt_token,
                'payload' : payload,
                'type': 'user'
                }
            )
        else:
            print("124")
            return Response(
              {'Error': "Invalid credentials"},
              status=400,
              content_type="application/json"
            )

class intermediatorLogin(generics.GenericAPIView):
    def get_tokens_for_intermediator(self, intermediator):
        refresh = RefreshToken.for_user(intermediator)

        return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
    serializer_class = serializers.intermediatorLoginSerializer
    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({"Error": "Please provide username/password"}, status="400")
        idd = request.data['intermediatorid']
        password = request.data['password']
        try:
            intermediator = models.intermediatorLogin.objects.get(intermediatorid=idd, password=password)
        except:
                return Response({"Error": "Invalid username/password"}, status="400")
        if intermediator:
            jwt_token = self.get_tokens_for_intermediator(intermediator)
            payload = jwt.decode(jwt_token['access'], 'SECRET_KEY')
            return Response({
                "access" : jwt_token,
                'payload' : payload,
                'type': 'intermediator'
                }
            )
        else:
            print("124")
            return Response(
              {'Error': "Invalid credentials"},
              status=400,
              content_type="application/json"
            )
