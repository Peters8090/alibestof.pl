from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline, OrderedInlineModelAdminMixin

from .models import Subcategory, Category


class SubcategoryAdmin(OrderedTabularInline):
    model = Subcategory
    extra = 0
    fields = ('name', 'move_up_down_links')
    readonly_fields = ('move_up_down_links',)
    sortable_by = []


@admin.register(Category)
class CategoryAdmin(OrderedInlineModelAdminMixin, OrderedModelAdmin):
    list_display = ('name', 'id', 'move_up_down_links')
    inlines = [SubcategoryAdmin]
    sortable_by = []
