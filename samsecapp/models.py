from django.db import models

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    emailAddress = models.EmailField()
    phoneNumber = models.CharField(max_length=100)

    def __str__(self):
        return self.firstName+""+self.lastName


