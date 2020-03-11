from rest_framework import serializers
from .models import beneficiaries
fields='__all__'
class beneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=beneficiaries
        fields='__all__'
        
        
       
    
    