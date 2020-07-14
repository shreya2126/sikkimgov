from django.contrib import admin
from .models import beneficiaries,UserLogin
from sikkimgov.models import Intermediatorloginform
admin.site.register(beneficiaries)
admin.site.register(Intermediatorloginform)
# Register your models here.
admin.site.register(UserLogin)