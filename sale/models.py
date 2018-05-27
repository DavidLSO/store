from django.contrib.auth.models import User
from django.db import models

from stoke.models import Items


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)

    def __str__(self):
        return str(self.items.count())


class Order(models.Model):
    STATUS_CHOICE = (
        ('Pedido Realizado', 'Pedido Realizado'),
        ('Separação em estoque', 'Separação em estoque'),
        ('Em montagem', 'Em montagem'),
        ('Realização de testes', 'Realização de testes'),
        ('Concluído', 'Concluído'),
    )
    code = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)
    status = models.CharField(max_length=150, choices=STATUS_CHOICE, default='Pedido Realizado')

    def __str__(self):
        return 'Order: {}'.format(self.code)

    @staticmethod
    def verify_requirement(cart):
        result = True
        for category in Items.CATEGORY_CHOICES:
            if not cart.items.filter(category=category[0]).exists():
                result = False
                break
        return result
