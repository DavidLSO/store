from django.db import models


class Stoke(models.Model):
    amount = models.IntegerField(verbose_name='Quantidade')

    def __str__(self):
        return str(self.amount)


class Items(models.Model):
    CATEGORY_CHOICES = (
        ('1', 'Processadores'),
        ('2', 'Memória RAM'),
        ('3', 'Disco Rígido/SSD'),
        ('4', 'Placa de Vídeo'),
        ('5', 'Gabinete'),
        ('6', 'Placa mãe'),
        ('7', 'Fonte')
    )
    name = models.CharField(max_length=255, verbose_name='Nome')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name='Categorias')
    value = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')
    stoke = models.OneToOneField(Stoke, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
