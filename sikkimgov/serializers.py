from rest_framework import serializers
from .models import beneficiaries
from .models import Intermediatorloginform

class beneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=beneficiaries
        fields='__all__'
        
class IntermediatorloginformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Intermediatorloginform
        fields='__all__'       
       
    
    