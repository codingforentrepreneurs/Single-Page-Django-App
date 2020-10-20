import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.urls import path


# https://docs.djangoproject.com/en/dev/topics/settings/#using-settings-without-setting-django-settings-module
settings.configure(
    DEBUG=True,
    SECRET_KEY = 'w^h13cf0p8fl^98raarj#-u$c6e!)l@1rl!+9j^a%rrb*8xpe3',
    ALLOWED_HOSTS=['*'],
    ROOT_URLCONF=__name__,
)

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About World</h1>")

urlpatterns = [
    path("", home_view),
    path("about/", about_view)
]


application = get_wsgi_application()

if __name__ == "__main__":
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)