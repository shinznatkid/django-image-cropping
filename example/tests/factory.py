from __future__ import unicode_literals
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
from example.models import Image


def create_cropped_image(**kwargs):
    defaults = {
        'image_cropping': '50,50,170,100',  # size: 120x100  as in model.py
        'image_path': '%s%s' % (settings.STATIC_ROOT, "/images/example_image.jpg"),
        'image_name': 'example_image',
    }
    defaults.update(kwargs)
    image = Image.objects.create(**{'cropping': defaults['image_cropping']})
    image.image_field.save(
        defaults['image_name'],
        File(open(defaults['image_path'], 'rb')))
    return image


def create_superuser(**kwargs):
    defaults = {
        'password': 'admin',
        'username': 'admin',
        'email': 'admin@admin.test',
    }
    defaults.update(kwargs)
    return User.objects.create_superuser(**defaults)
