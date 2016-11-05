from __future__ import unicode_literals

from django.db import models

FONT_CHOICES = (
	('comic', 'Comic'),
	('grunge', 'Grunge'),
	('pixel', 'Pixel'),
    ('sans', 'Sans'),
    ('script', 'Script'),
    ('serif', 'Serif'),
	('slab', 'Slab'),    
)

class First(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=100)
    font = models.CharField(choices=FONT_CHOICES, default='sans', max_length=100)

    class Meta:
        ordering = ('created',)

class Last(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=100)
    font = models.CharField(choices=FONT_CHOICES, default='sans', max_length=100)

    class Meta:
        ordering = ('created',)

class Title(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=100)
    font = models.CharField(choices=FONT_CHOICES, default='sans', max_length=100)

    class Meta:
        ordering = ('created',)

