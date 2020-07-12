from django.contrib import admin
from .models import beneficiaries
from sikkimgov.models import Intermediatorloginform
admin.site.register(beneficiaries)
admin.site.register(Intermediatorloginform)
# Register your models here.
