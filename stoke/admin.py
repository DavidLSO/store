from django.contrib import admin
from stoke.models import Items, Stoke


def item_name(obj):
    return obj.items.name


@admin.register(Stoke)
class StokeInline(admin.ModelAdmin):
    list_display = (item_name, 'amount')


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    pass
