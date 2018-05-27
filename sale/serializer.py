from django.contrib.auth.models import User
from rest_framework import serializers

from stoke.serializer import ItemsSerializer
from sale.models import Cart, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class CartSerializer(serializers.HyperlinkedModelSerializer):
    products = ItemsSerializer(read_only=True, many=True, source='items')
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['products']

    def get_total(self, obj):
        result = 0
        for i in obj.items.all():
            result += i.value
        return result


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['code']
