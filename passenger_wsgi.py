import sys, os

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "alibestof_pl.settings"  # zmienić 'nazwa_aplikacji' na
                                                                   # nazwę projektu Django 

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()