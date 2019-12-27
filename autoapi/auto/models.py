from django.db import models
from django.urls import reverse

# Create your models here.


class Marka(models.Model):
    marka = models.CharField(max_length=250, db_index=True)
    object = models.Manager()

    class Meta:
        ordering = ['marka']

    def __str__(self):
        return self.marka


class Modell(models.Model):
    model = models.CharField(max_length=250, db_index=True)
    object = models.Manager()

    class Meta:
        ordering = ['model']

    def __str__(self):
        return self.model

class Order(models.Model):

    CATEGORY_CHOICES = (
        ('to 1990', ' To 1990'),
        ('from 1990 to 2000', 'From 1990 to 2000'),
        ('from 2000 to 2010', 'From 2000 to 2010'),
        ('after 2010', 'After 2010')
    )
    autor_name = models.CharField(max_length=250, db_index=True)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE,related_name='markas')
    model = models.ForeignKey(Modell, on_delete=models.CASCADE,related_name='models')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='to 1990')
    release = models.DateField(auto_now_add=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    object = models.Manager()

    def get_absolute_url(self):
        return reverse('auto:order_detail', args=[self.id])

    class Meta:
        unique_together = ['marka', 'model']
        ordering = ['autor_name']

    def __str__(self):
        return self.autor_name

