from django.contrib import admin

from .models  import  *


class ItemsAdmin(admin.ModelAdmin):
    list_display=('itemName', 'itemCode', 'itemPrice')

admin.site.register(Items, ItemsAdmin)

class ordersAdmin(admin.ModelAdmin):
    list_display=('id', 'itemCode', 'itemName', 'itemPrice', 'totalPrice')

admin.site.register(Orders, ordersAdmin)