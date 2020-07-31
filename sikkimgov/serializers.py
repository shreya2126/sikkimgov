from rest_framework import serializers
from .models import beneficiaries,initial
from .models import Intermediatorloginform,UserLogin,intermediatorLogin


class beneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=beneficiaries
        fields=('id','firstname', 'lastname', 'phoneno', 'address', 'adhaarno', 'bankname', 'accountno', 'IFSC', 'areafland','longitude','latitude', 'adhaarimage', 'registryimage' )


class initialSerializer(serializers.ModelSerializer):

    class Meta:
        model= initial
        fields = ('id', 'img')

        
class IntermediatorloginformSerializer(serializers.ModelSerializer):
    class Meta:
        adhaarimage = serializers.ImageField
        model=Intermediatorloginform
        fields='__all__'       
       
class intermediatorUpdate(serializers.Serializer):
    firstname = serializers.CharField
    lastname=serializers.CharField
    fathername=serializers.CharField
    contactno=serializers.IntegerField
    alternatecontactno=serializers.IntegerField
    adhaarno=serializers.IntegerField
    email=serializers.CharField
    state=serializers.CharField
    district=serializers.CharField
    region=serializers.IntegerField
    dateofbirth=serializers.DateField  
    adhaarimage=serializers.ImageField


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLogin
        fields='__all__'

class intermediatorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=intermediatorLogin
        fields='__all__'                



    