from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = models.TextField(blank=True, verbose_name='Полное описание (HTML)')
    lng = models.DecimalField(
        max_digits=17, decimal_places=14,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        verbose_name='Долгота',
    )
    lat = models.DecimalField(
        max_digits=17, decimal_places=14,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        verbose_name='Широта',
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='imgs', on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to='places/%Y/%m/%d/', verbose_name='Картинка')
    position = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Порядок')

    class Meta:
        ordering = ['position', 'id']
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения места'

    def __str__(self):
        return f'{self.place} — {self.position}'
