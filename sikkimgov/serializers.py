from rest_framework import serializers
from .models import beneficiaries
from .models import Intermediatorloginform,UserLogin,intermediatorLogin



class beneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=beneficiaries
        fields='__all__'
        
class IntermediatorloginformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Intermediatorloginform
        fields='__all__'       
       
    
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLogin
        fields='__all__'

class intermediatorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=intermediatorLogin
        fields='__all__'                



    