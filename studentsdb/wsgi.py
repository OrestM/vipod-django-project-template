<<<<<<< HEAD
"""
=======
﻿"""
>>>>>>> 58be2f64b9e85d2fc89693035b62c5a192cfae8c
WSGI config for studentsdb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentsdb.settings")

application = get_wsgi_application()
