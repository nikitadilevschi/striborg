from django.db import models

from wagtail.models import Page


class HomePage(Page):

    subtitle = models.CharField(max_length=100, blank=True, null=True)
