import sys
import os

from django.conf import settings
from django.urls import path
from django.shortcuts import render

settings.configure(
        DEBUG=True,
        SECRET_KEY=str(os.urandom(32)),
        ROOT_URLCONF=__name__,
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': ['']
                }
            ]
        )

def index(request):
    return render(request, 'index.html')

urlpatterns = [
        path('', index),

        ]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


