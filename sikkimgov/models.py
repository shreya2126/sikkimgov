from django.db import models
from django.db import models





# Create your models here.
class beneficiaries(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phoneno=models.IntegerField()
    address=models.CharField(max_length=200)
    adhaarno=models.IntegerField(primary_key=True)
    bankname=models.CharField(max_length=50)
    accountno=models.IntegerField()
    IFSC=models.CharField(max_length=50)
    areafland=models.IntegerField()

    def _str_(self):
        return self.firstname

class Intermediatorloginform(models.Model):
    title=models.CharField(max_length=6)
    firstname=models.CharField(max_length=20)
    middlename=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    fathername =models.CharField(max_length=20)   
    mothername=models.CharField(max_length=20)
    contactno=models.IntegerField(max_length=10)
    alternatecontactno=models.IntegerField(max_length=10)
   # address=models.CharField(max_length=200)
    adhaarno=models.IntegerField(primary_key=True)
    email=models.CharField(max_length=10)
    state=models.CharField(max_length=200)
    district=models.CharField(max_length=200, null=True, blank=True)
    region=models.CharField(max_length=200)
    dateofbirth=models.DateField(null=True, blank=True)
    image=models.ImageField(upload_to='image')

