from django.db import models


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name='Категория')
    min_date = models.SmallIntegerField(verbose_name='min_date')
    max_date = models.SmallIntegerField(verbose_name='max_date')

    object = models.Manager()

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CarMarka(models.Model):
    car_marka = models.CharField(max_length=255, verbose_name='Марка авто')

    def __str__(self):
        return self.car_marka

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марка авто'


class CarModel(models.Model):
    car_model = models.CharField(max_length=255, verbose_name='Модель авто')

    def __str__(self):
        return self.car_model

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модель авто'


class Car(models.Model):
    price = models.SmallIntegerField(verbose_name='Цена')
    year = models.SmallIntegerField(verbose_name='Год выпуска')
    name = models.CharField(max_length=255, verbose_name='Имя владельца')

    car_cat = models.CharField(verbose_name='Категория', max_length=255, default='do 1990')
    car_marka = models.ForeignKey(CarMarka, verbose_name='Марка', related_name='car_marks', on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, verbose_name='Модель', related_name='car_models', on_delete=models.CASCADE)

    object = models.Manager()

    def save(self, *args, **kwargs):
        cat = Category.object.all()
        car_category = ''
        for i in cat:
            if i.max_date >= int(self.year) >= i.min_date:
                car_category = i.category
        self.car_cat = car_category
        super(Car, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'



