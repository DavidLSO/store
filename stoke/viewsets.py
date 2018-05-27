from rest_framework import viewsets

from .models import Items
from .serializer import ItemsSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Items.objects.filter(stoke__amount__gt=0)
