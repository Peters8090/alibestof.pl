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

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True
