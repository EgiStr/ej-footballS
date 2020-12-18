from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Costumer(models.Model):
    """
    docstring
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    nameD = models.CharField(max_length=50)
    nameB = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, default='nameD')
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    email = models.EmailField(blank=True, null=True)
    nomorhp = models.IntegerField(blank=True, null=True)
    profil = models.ImageField(upload_to='media/image',
                               height_field='height_field', width_field='width_field', max_length=None, default='media/image/IMG_20191007_233026_695.jpg')
    background = models.ImageField(
        upload_to='media/bgimg', height_field='height_field2', width_field='width_field2', default='media/image/IMG_20191007_233026_695.jpg')
    height_field = models.IntegerField(default=0)
    height_field2 = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    width_field2 = models.IntegerField(default=0)

    def fullname(self):
        return str(self.nameD) + str(self.nameB)

    def __str__(self):
        return f'{self.id}.{self.user}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_Costumer(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Costumer.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_Costumer(sender, instance, **kwargs):
    # instance.Costumer.save()
    pass


# def Costumer_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         Costumer = Costumer.objects.create(user=instance)
#     else:
#         instance.Costumer.save()

# post_save.connect(Costumer_receiver, sender=settings.AUTH_USER_MODEL)
