from django.conf import settings


def context_processor(request):
    return {
        'themes': settings.BOOTSWATCH_THEMES,
        'current_theme': request.session.get('theme', 'superhero')
    }
