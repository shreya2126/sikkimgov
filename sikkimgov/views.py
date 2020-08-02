from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import beneficiaries
from .models import Intermediatorloginform
from .models import intermediatorLogin,initial
from django.views.decorators.csrf import csrf_exempt
from .serializers import beneficiariesSerializer , beniSerializer
from .serializers import IntermediatorloginformSerializer,intermediatorLoginSerializer,initialSerializer
from datetime import datetime
import json
from . import models
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from . import models,serializers
from rest_framework import generics
from rest_framework.authentication import get_authorization_header
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
import django_filters
from .ml import *



class benefViewSet(APIView):
    def get(self, request, format=None):
        obj = initial.objects.all()
        serializer = beniSerializer(obj, many=True)
        predict = "No image posted! Post an image."
        response = {'prediction': predict, 'data': serializer.data}
        return Response(response)

    def post(self, request, format=None):
        serializer = beniSerializer(data=request.data)
        predict = 'No image posted!'
        if serializer.is_valid():
            serializer.save()
            imgname = str(request.data['img']).replace(" ", "_").replace("(", "").replace(")", "")

            try:
                path = r"C:\Users\HP\sikkimgov\serve\media-root\initial" + '\\' + imgname
            except:
                path = None

            if path is not None:
                if path[-2] == 'p' or path[-2] == 'P' or path[-2] == 'e' or path[-2] == 'E' or path[-2] == 'n' or \
                        path[-2] == 'N':
                    predict = throw_result(path)
                else:
                    predict = "Image must be in jpg or jpeg or png format!"
            response = {'prediction': predict, 'data': serializer.data}
            try:
                obj = get_object_or_404(beneficiaries, adhaarno=int(request.data['beni_adhar']))
                print(obj)
                obj.level = predict
                obj.save()
            except:
                pass

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class initialViewSet(APIView):
    def get(self, request, format=None):
        obj = initial.objects.all()
        serializer = initialSerializer(obj,many=True)
        predict = "No image posted! Post an image."
        response = {'prediction': predict, 'data': serializer.data}
        return Response(response)

    def post(self, request, format=None):
        serializer = initialSerializer(data=request.data)
        predict = 'No image posted!'
        if serializer.is_valid():
            serializer.save()
            imgname = str(request.data['img']).replace(" ", "_").replace("(", "").replace(")", "")

            try:
                path = r"C:\Users\HP\sikkimgov\serve\media-root\initial" + '\\' + imgname
            except:
                path = None

            if path is not None:
                if path[-2] == 'p' or path[-2] == 'P' or path[-2] == 'e' or path[-2] == 'E' or path[-2] == 'n' or \
                        path[-2] == 'N':
                    predict = throw_result(path)
                else:
                    predict = "Image must be in jpg or jpeg or png format!"
            response = {'prediction': predict, 'data': serializer.data}
            try:
                obj = get_object_or_404(initial, img__endswith=imgname)
                print(obj)
                obj.delete()
            except:
                pass

            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class benViewSet(viewsets.ModelViewSet):
    serializer_class = beneficiariesSerializer
    queryset = beneficiaries.objects.all()
    lookup_field='id'


class BenView(generics.ListAPIView):
    serializer_class = beneficiariesSerializer
    def get_queryset(self):
        idd = self.request.GET.get('id')
        return models.beneficiaries.objects.filter(id=idd)
   
def BenGet(request):
    idd = request.GET.get('id')
    data = models.beneficiaries.objects.filter(id=idd)    
   

class beneficiaries(generics.ListCreateAPIView):
    status=(status.HTTP_201_CREATED)
    #     return Response(serializer.data)   
    serializer_class = beneficiariesSerializer
    

    def post(self,request,args,*kwargs):
        import random
        otp = random.randint(111111,999999)
        #send the message here
        firstname = request.data['firstname']
        lastname=request.data['lastname']
        phoneno=request.data['phoneno']
        address=request.data['address']
        adhaarno=request.data['adhaarno']
        bankname=request.data['bankname']
        accountno=request.data['accountno']
        IFSC=request.data['IFSC']
        areafland=request.data['areafland']
        adhaarimage=request.data['adhaarimage']
        registryimage=request.data['registryimage']

        try:
            user = models.beneficiaries.objects.create(firstname=firstname,otp=otp,lastname=lastname,phoneno=phoneno,address=address,
            
            adhaarno=adhaarno,bankname=bankname,accountno=accountno,IFSC=IFSC,areafland=areafland,adhaarimage=adhaarimage,registryimage=registryimage
            )
        except:
            raise
        

            url = "https://www.fast2sms.com/dev/bulk"

            payload = "sender_id=FSTSMS&language=english&route=qt&numbers=9729134259&message=32637 &variables={#BB#}&variables_values=5252"
            headers = {
            'authorization': "F2mBgj87SD5aXPklRJsUh4duG0fYVcvK9Cqpn6tiTWzNLHZ1by4V8BmU1ZMAI52n3vhOLzyo0kYDiRrf",
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
    }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

        # user = models.beneficiaries.objects.create(lastname=lastname,otp=otp)   
      
        return Response({'success': 'otp sent','payload': user.id})
    def get_queryset(self):
        idd = self.request.GET.get('id')
        if idd:
            return models.beneficiaries.objects.filter(id=idd)
        queryset =  models.beneficiaries.objects.all()
        return queryset

    def get_object(self):
        idd = self.kwargs['pk']
        return self.get_queryset().filter(id=idd)    
        
from rest_framework import exceptions
from rest_framework.decorators import api_view
@api_view(['POST'])
def Verify(request):
    idd = request.GET.get('id')
    otp = request.data.get('otp')
    print(idd,otp)
    if not otp and not id:
        raise exceptions.NotAcceptable('error')
    try:
        user = models.beneficiaries.objects.get(id=int(idd),otp=str(otp))
    except:
        raise exceptions.NotAcceptable('error')
    user.status="verified"
    user.save()
    return Response({'success':'otp verified'})

class intermediatorViewSet(viewsets.ModelViewSet):
    serializer_class = IntermediatorloginformSerializer
    queryset = Intermediatorloginform.objects.all()
    lookup_field = 'id'

class intermediatorUpdate(generics.CreateAPIView):
    serializer_class = serializers.intermediatorUpdate
    def post(self,request,args,*kwargs):
        token = get_authorization_header('Authorization')
        if token == b'':
            raise           #raise the exception here
            try:
                idd = jwt.decode('SECRET_KEY',token)
            except:
                pass
                userid = request.GET.get('id')
                firstname = request.data['firstname']
        
                lastname=request.data['lastname']
                contactno=request.data['contactno']
                alternatecontactno=request.data['alternatecontactno']
                adhaarno=request.data['adhaarno']
                email=request.data['email']
                state=request.data['state']
                region=request.data['region']
                dateofbirth=request.data['dateofbirth']
                adhaarimage=request.data['adhaarimage']
        

        #get all the data here
        try:
            user = models.Intermediatorloginform.objects.get(id=userid)
        except:
            pass
        user.firstname=firstname
        user.lastname=lastname
        user.contactno=contactno
        user.alternatecontactno=alternatecontactno
        user.adhaarno=adhaarno
        user.email=email
        user.state=state
        user.district=district
        user.region=region
        user.dateofbirth=dateofbirth
        user.adhaarimage=adhaarimage
        
        #set all the fields here
        user.save()
        return Response({'success':'updated'})

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
