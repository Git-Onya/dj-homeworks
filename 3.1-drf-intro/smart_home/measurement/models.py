from django.db import models


class Sensor(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=255, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField('Температура')
    created_at = models.DateTimeField('Дата измерения', auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',
                               verbose_name='Номер сенсора')
    sensor_image = models.ImageField('Фото показаний', blank=True, max_length=255)

    def __str__(self):
        return f'measurement by {self.sensor} at {self.created_at}'
