from rest_framework import serializers
from .models import beneficiaries
from .models import Intermediatorloginform,UserLogin,intermediatorLogin


class beneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        adhaarimage = serializers.ImageField
        registryimage=serializers.ImageField
        model=beneficiaries
        fields="firstname","lastname","phoneno","address","adhaarno","bankname","accountno","IFSC","areafland","adhaarimage","registryimage"
 
class BenUpdate(serializers.ModelSerializer):        
    firstname = serializers.CharField
    lastname=serializers.CharField
    phoneno=serializers.IntegerField
    address=serializers.CharField
    adhaarno=serializers.IntegerField
    bankname=serializers.CharField
    accountno=serializers.IntegerField
    IFSC=serializers.CharField
    areafland=serializers.IntegerField
    adhaarimage=serializers.ImageField
    registryimage=serializers.ImageField

    
    

        
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



    