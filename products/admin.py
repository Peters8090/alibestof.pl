from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',  'description', 'user', 'date_modified', 'date_created', 'published')
    list_filter = ['user', 'date_created', 'date_modified', 'published']
    search_fields = ['name', 'description']

    # display only products the user owns
    def get_queryset(self, request):
        super().get_queryset(request)
        if request.user.is_superuser:
            return Product.objects
        else:
            return Product.objects.filter(user_id=request.user.id)

    # auto assign user to the one creating the product
    def save_model(self, request, obj, form, change):
        try:
            obj.user
        except ObjectDoesNotExist:
            obj.user = request.user
        print(change)
        super().save_model(request, obj, form, change)
