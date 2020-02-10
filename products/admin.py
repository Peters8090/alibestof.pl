from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'id', 'user', 'author', 'category', 'description', 'product_link', 'photos_link', 'date_modified',
        'date_created', 'published')
    list_filter = ['user', 'author', 'category', 'date_modified', 'date_created', 'published']
    list_editable = ['description', 'product_link', 'photos_link', ]
    search_fields = ['name', 'description']
    actions = ['publish_products', 'unpublish_products']

    def publish_products(self, request, queryset):
        p = queryset.update(published=True)
        self.message_user(request, f'{p} products published')

    def unpublish_products(self, request, queryset):
        p = queryset.update(published=False)
        self.message_user(request, f'{p} products unpublished')

    publish_products.short_description = 'Publish selected products'
    unpublish_products.short_description = 'Unpublish selected products'

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
        super().save_model(request, obj, form, change)