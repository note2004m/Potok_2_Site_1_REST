from django.contrib import admin

from apps.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_username', 'title', 'price')

    def get_user_username(self, obj):
        return obj.user.username if obj.user else "—"
    get_user_username.short_description = "Пользователь"