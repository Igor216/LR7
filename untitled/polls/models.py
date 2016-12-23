from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class BankModel(models.Model):
    idbank = models.IntegerField(primary_key=True)
    director = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.address)


class TransactionModel(models.Model):
    idtran = models.IntegerField(primary_key=True)
    sum = models.IntegerField()
    type = models.CharField(max_length=50)
    user = models.ForeignKey('User')
    bank = models.ForeignKey('BankModel')
    date = models.DateTimeField()

    def __str__(self):
        return str(self.sum)
