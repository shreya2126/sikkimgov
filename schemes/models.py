from django.db import models
from jsonfield import JSONField
# Create your models here.
class Schemes(models.Model):
    Title = models.CharField(max_length=5000)
    Description = models.TextField()
    Requirement = models.TextField()
    Pic = models.ImageField(upload_to="images")
    Eligibility = JSONField()
    Feature = models.TextField()
    needs = models.TextField()
    intermediator = JSONField()


    def __str__(self):
        return self.Title