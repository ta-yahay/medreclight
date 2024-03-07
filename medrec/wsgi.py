"""
WSGI config for medrec project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# settings_module='medrec.azuredep' if 'WEBSITE_HOSTNAME' in os.environ else 'medrec.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medrec.settings')

application = get_wsgi_application()
