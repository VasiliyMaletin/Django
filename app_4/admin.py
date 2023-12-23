from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_registered']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity']
    list_filter = ['price', 'quantity']
    ordering = ['-price', 'quantity']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по названию и описанию'
    readonly_fields = ['date_added']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description'],
            },
        ),
        (
            'О товаре',
            {
                'fields': ['date_added', 'price', 'quantity']
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
