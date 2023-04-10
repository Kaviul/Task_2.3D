from django.db import models

# Create your models here.


class Student(models.Model):
    givenName = models.CharField(max_length=50)
    familyName = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    contact = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.givenName + ' ' + self.familyName + ' ' + self.sex + ' ' + self.email + ' ' + self.contact + ' ' + self.address
