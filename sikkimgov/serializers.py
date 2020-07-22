from rest_framework import serializers
from .models import beneficiaries,initial
from .models import Intermediatorloginform,UserLogin,intermediatorLogin
from django.contrib.auth.models import User, Group


class beneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=beneficiaries
        fields=( 'firstname', 'lastname', 'phoneno', 'address', 'adhaarno', 'bankname', 'accountno', 'IFSC', 'areafland', 'adhaarimage', 'registryimage', 'phase1', 'phase2', 'phase3', 'phase4', 'phase5', 'phase6' )


class callSerializer(serializers.ModelSerializer):

    class Meta:
        model= initial
        fields = ('id', 'img', 'intrmed_adhaar')
        
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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
    