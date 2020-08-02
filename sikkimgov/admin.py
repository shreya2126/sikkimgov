from django.contrib import admin
from .models import beneficiaries,UserLogin,intermediatorLogin
from sikkimgov.models import Intermediatorloginform,initial
admin.site.register(beneficiaries)
admin.site.register(Intermediatorloginform)
# Register your models here.
admin.site.register(UserLogin)
admin.site.register(intermediatorLogin)
admin.site.register(initial)