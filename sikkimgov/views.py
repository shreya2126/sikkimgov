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
from rest_framework.authentication import get_authorization_header


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

class benViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.beneficiaries
    queryset = beneficiaries.objects.all()

class benUpdate(generics.CreateAPIView):
    serializer_class = serializers.BenUpdate
    def post(self,request,*args,**kwargs):
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
        phoneno=request.data['phoneno']
        address=request.data['address']
        adhaarno=request.data['adhaarno']
        bankname=request.data['bankname']
        accountno=request.data['accountno']
        IFSC=request.data['IFSC']
        areafland=request.data['areafland']
        adhaarimage=request.data['adhaarimage']
        registryimage=request.data['registryimage']

        #get all the data here
        try:
            user = models.beneficiaries.objects.get(id=userid)
        except:
            pass
        user.firstname=firstname
        user.lastname=lastname
        user.phoneno=phoneno
        user.address=address
        user.adhaarno=adhaarno
        user.bankname=bankname
        user.accountno=accountno
        user.IFSC=IFSC
        user.areafland=areafland
        user.adhaarimage=adhaarimage
        user.registryimage=registryimage
        #set all the fields here
        user.save()
        return Response({'success':'updated'})

    #do this for intermediate login form and you are done 

class beneficiaries(generics.ListCreateAPIView):
    status=(status.HTTP_201_CREATED)
    #     return Response(serializer.data)   
    serializer_class = beneficiariesSerializer

    def post(self,request,*args,**kwargs):
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
        from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
        account_sid = 'AC7095a7f37c92f9f251b61fcc847ab524'
        auth_token = '72a7a22a198f792a50507949d51c94c2'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=otp,
                                    from_='+19284400322',
                                    to='+91'+str(phoneno)
                                )

        print(message.sid)
        # user = models.beneficiaries.objects.create(lastname=lastname,otp=otp)   
        # user = models.beneficiaries.objects.create(phoneno=phoneno,otp=otp)   
        # user = models.beneficiaries.objects.create(address=address,otp=otp)   
        # user = models.beneficiaries.objects.create(adhaarno=adhaarno,otp=otp)   
        # user = models.beneficiaries.objects.create(bankname=bankname,otp=otp)   
        # user = models.beneficiaries.objects.create(accountno=accountno,otp=otp)  
        # user = models.beneficiaries.objects.create(IFSC=IFSC,otp=otp)   
        # user = models.beneficiaries.objects.create(areafland=areafland,otp=otp)    
        # user = models.beneficiaries.objects.create(adhaarimage=adhaarimage,otp=otp)   
        # user = models.beneficiaries.objects.create(registryimage=registryimage,otp=otp)   
         #create the user here

        return Response({'success': 'otp sent','payload': user.id})
    def get_queryset(self):
        idd = self.request.GET.get('id')
        if idd:
            return models.beneficiaries.objects.filter(id=idd)
        queryset =  models.beneficiaries.objects.all()
        return queryset
        
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
    serializer_class = serializers.Intermediatorloginform
    queryset = Intermediatorloginform.objects.all()

class intermediatorUpdate(generics.CreateAPIView):
    serializer_class = serializers.BenUpdate
    def post(self,request,*args,**kwargs):
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

class Intermediatorloginform(generics.ListCreateAPIView):
    status=(status.HTTP_201_CREATED)
    #     return Response(serializer.data)   
    serializer_class = IntermediatorloginformSerializer
    def get_queryset(self):
        idd = self.request.GET.get('id')
        print(idd)
        if idd:
            return models.Intermediatorloginform.objects.filter(id=idd)
        queryset =  models.Intermediatorloginform.objects.all()
        return queryset
        

    
  
class intermediatorlogindetail(APIView):
    def get(self,request,intermediator_id):
        intermediatorloginform=Intermediatorloginform.objects.get(id=intermediator_id)
        serializer=IntermediatorloginformSerializer(intermediatorloginform)
        return Response(serializer.data)

    def put(self,request,intermediator_id):
        serializer=IntermediatorloginformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

