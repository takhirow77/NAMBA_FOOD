from django.db import models

# Create your models here.
class Contacts(models.Model):
    description = models.TextField(
        verbose_name="Описание"
    )
    email = models.EmailField(
        verbose_name="почта"
    )
    phone_number = models.PositiveBigIntegerField(
        verbose_name="Номер телефона"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"