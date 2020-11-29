from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Costumer(models.Model):
    """
    docstring
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    nameD = models.CharField(max_length=50)
    nameB = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, default='nameD')
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    email = models.EmailField()
    nomorhp = models.IntegerField()
    profil = models.ImageField(upload_to='media/image',
                               height_field='height_field', width_field='width_field', max_length=None)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def fullname(self):
        return str(self.nameD) + str(self.nameB)

    def __str__(self):
        return f'{self.id}.{self.user}'
