from django.contrib import admin

from orders.models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['created', 'paid']
    inlines = [OrderItemInline]


admin.site.register(Order)