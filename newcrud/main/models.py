from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """При создании нового пользователя создает его токен аутентификации
    и профайл"""
    if created:
        Token.objects.create(user=instance)
        Profile.objects.get_or_create(username=instance)


class Company(models.Model):

    name = models.CharField(verbose_name="Название компании", max_length=250)
    about = models.TextField(verbose_name="О компании", blank=True)


class News(models.Model):

    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название новости", max_length=250)
    news = models.TextField(verbose_name="Описание новости")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Profile(models.Model):

    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Имя пользователя"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Компания"
    )
