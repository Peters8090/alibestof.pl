from .models import Configuration, SocialLink


def base(request):
    social_links = SocialLink.objects.all().filter()
    return {
        'social_links': social_links,
    }
