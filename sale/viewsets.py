import uuid

from django.db import transaction
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sale.serializer import CartSerializer, OrderSerializer
from stoke.models import Items
from .models import Cart, Order


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    @action(methods='get', detail=True)
    def get_cart(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        if cart:
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            return Response([])

    @action(methods='post', detail=True)
    def add_item(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        item = request.POST.get('item')
        if item:
            cart.items.add(Items.objects.get(id=int(item)))
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            return Response([])

    @action(methods='post', detail=True)
    def remove_item(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        item = request.POST.get('item')
        if item:
            cart.items.remove(Items.objects.get(id=int(item)))
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            return Response([])


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    @action(methods='get', detail=True)
    def get_order(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user)
        if order.count() > 0:
            result = []
            for o in order:
                result.append({
                    'code': o.code,
                    'status': o.status
                })
            return Response(result)
        else:
            return Response([])

    @action(methods='post', detail=True)
    def create_order(self, request, *args, **kwargs):
        user = request.user
        if user:
            cart = user.cart
            if Order.verify_requirement(cart):
                order = Order()
                order.user = user
                order.code = uuid.uuid4()
                order.save()
                for i in cart.items.all():
                    order.items.add(i)

                cart.delete()
                transaction.commit()
                return Response('Order created')
            else:
                raise serializers.ValidationError({"items": "É mecessário possuir um item de cada categoria."})
        else:
            return Response([])
