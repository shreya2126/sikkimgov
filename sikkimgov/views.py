from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import beneficiaries as beneficiaries2
from django.views.decorators.csrf import csrf_exempt
from .serializers import beneficiariesSerializer 
from datetime import datetime
from sikkimgov.models import Intermediatorloginform

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
    def get(self, request):
        beneficiaries1=beneficiaries2.objects.all()
        serializer=beneficiariesSerializer(beneficiaries1, many=True)
        return Response(serializer.data)

def home(request):
    # request.session['fav_color'] = 'blue'
    #form =AuthenticationForm()
    #print ('dsaad =>  ', request.session['fav_color'])
    return render(request,'home.html')




def intermediatorloginform(request):
    if request.method =="POST":
        intermediatorloginform=Intermediatorloginform()

        intermediatorloginform.title=request.POST.get('title')
        intermediatorloginform.firstname=request.POST.get('firstname')
        intermediatorloginform.middlename=request.POST.get('middlename')
        intermediatorloginform.lastname=request.POST.get('lastname')
        intermediatorloginform.fathername=request.POST.get('fathername')
        intermediatorloginform.mothername=request.POST.get('mothername')
        intermediatorloginform.contactno=request.POST.get('contactno')
        intermediatorloginform.alternatecontactno=request.POST.get('alternatecontactno')
        #intermediatorloginform.address=request.POST.get('address')
        intermediatorloginform.adhaarno=request.POST.get('adhaarno')
        intermediatorloginform.email=request.POST.get('email')
        intermediatorloginform.state=request.POST.get('state')
        intermediatorloginform.district=request.POST.get('district')
        intermediatorloginform.region=request.POST.get('region')
        intermediatorloginform.dateofbirth=request.POST.get('dateofbirth')
        intermediatorloginform.image=request.POST.get('image')
       # intermediatorloginform=Intermediatorloginform(title=title, firstname=firstname, middlename=middlename, lastname=lastname, fathername=fathername, mothername=mothername, contactno=contactno, alternatecontactno=alternatecontactno, address=address, adhaarno=adhaarno, email=email, state=state, district=district, region=region, dateofbirth=dateofbirth)
        intermediatorloginform.save()

    return render(request,'intermediatorloginform.html')

