"""
WSGI config for vainu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/fromsujay/myvenv/vainu'

if path not in sys.path:
    sys.path.append(path) 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vainu.settings")

application = get_wsgi_application()
