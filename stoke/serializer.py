from rest_framework import serializers
from .models import Items


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.SerializerMethodField('get_category')

    class Meta:
        model = Items
        fields = ['name', 'category_name', 'value']

    def get_category(self, obj):
        result = ''
        for i in Items.CATEGORY_CHOICES:
            if obj.category == i[0]:
                result = i[1]
        return result
