from django.contrib import admin

from .models import Configuration, SocialLink

admin.site.site_header = "AliBestOf"
admin.site.index_title = "Administration"
admin.site.site_title = "AliBestOf"


class SocialLinksInline(admin.TabularInline):
    model = SocialLink
    extra = 0


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    inlines = [SocialLinksInline]
    fieldsets = (
        ('Basic', {
            'fields': ('home_page_user', 'product_duplication_superuser')
        }),
        ('Displaying products', {
            'fields': (
                'products_per_page',
                'product_link_validator',
                'photos_link_validator',)
        }),
    )

    # There can be only one Configuration
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True
