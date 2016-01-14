from __future__ import unicode_literals

from django.db import models


class Good(models.Model):
    name = models.TextField()
