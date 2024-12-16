from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField('Название', max_length=50)
    address = models.CharField('Адрес', max_length=200)
    capacity = models.IntegerField('Вместимость')
    size = models.CharField('Размер зала', max_length= 50)
    price = models.FloatField('Цена')
    image = models.ImageField('Изображение зала')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
