from django.db import models

# Create your models here.
class Schemes(models.Model):
    Title = models.CharField(max_length=5000)
    Description = models.CharField(max_length=50000)
    Requirement = models.CharField(max_length=50000)
    Pic = models.ImageField(upload_to="images")

    def __str__(self):
        return self.Title