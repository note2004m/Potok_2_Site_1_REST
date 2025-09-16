from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.db import models

User = get_user_model()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to= 'products/', verbose_name="Картинка")
    description = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"