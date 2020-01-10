from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        super().get_queryset(request)
        if request.user.is_superuser:
            return Product.objects
        else:
            return Product.objects.filter(user_id=request.user.id)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
