

from django.db import models

class beneficiaries(models.Model):
    id = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phoneno=models.IntegerField()
    address=models.CharField(max_length=200)
    adhaarno=models.IntegerField(unique=True)
    bankname=models.CharField(max_length=50)
    accountno=models.IntegerField()
    IFSC=models.CharField(max_length=50)
    areafland=models.IntegerField()
   
    adhaarimage=models.ImageField(upload_to='adhaarimage',null=True, blank=True)
    registryimage=models.ImageField(upload_to='registryimage',null=True, blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    
    status = models.CharField(max_length=20,default='pending')
    otp = models.CharField(max_length=20,null=True,blank=True,default=None)

class initial(models.Model):
    intrmed_adhaar = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to='initial/')
    # img =  models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.intrmed_adhaar)    


class Intermediatorloginform(models.Model):
    id = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    fathername =models.CharField(max_length=20)   
    contactno=models.IntegerField()
    alternatecontactno=models.IntegerField()
    adhaarno=models.IntegerField(unique=True)
    email=models.CharField(max_length=100)
    state=models.CharField(max_length=200)
    district=models.CharField(max_length=200, null=True, blank=True)
    region=models.CharField(max_length=200)
    dateofbirth=models.DateField(null=True, blank=True)
    adhaarimage=models.ImageField(upload_to='adhaarimage',null=True, blank=True)

class UserLogin(models.Model):
    userid = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=20)

class intermediatorLogin(models.Model):
    intermediatorid = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=20)    