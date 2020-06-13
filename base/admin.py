from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Configuration, SocialLink, Profile

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
                'how_to_buy',
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


@admin.register(Profile)
class UserProfileConfigurationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        super().get_queryset(request)
        if request.user.has_perm('base.can_interact_with_all_profiles'):
            return Profile.objects
        elif request.user.has_perm('base.can_interact_with_his_own_profile'):
            return Profile.objects.filter(user_id=request.user.id)
        else:
            return Profile.objects.none()

    def save_model(self, request, obj, form, change):
        try:
            obj.user
        except ObjectDoesNotExist:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if Profile.objects.filter(user__username__exact=request.user.username).count() > 0:
            return False
        else:
            return True
