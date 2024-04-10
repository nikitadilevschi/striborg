"""Menus models."""
from django.db import models

from django_extensions.db.fields import AutoSlugField
from wagtail.admin.panels import (FieldPanel,
                                  InlinePanel,
                                  MultiFieldPanel,
                                  PageChooserPanel)

from modelcluster.models import ClusterableModel
from wagtail.models import Page, ParentalKey, Orderable
from wagtail.snippets.models import register_snippet

class MenuItem(Orderable):

    link_title = models.CharField(max_length=50, null=True, blank=True)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+'
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey('Menu', related_name='menu_items')


    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]
    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing title'


@register_snippet
class Menu(ClusterableModel):
    """The main menu clustarable model."""
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
        ], heading='Menu'),
        InlinePanel('menu_items', label='Menu Items'),
    ]
    def __str__(self):
        return self.title

class FooterItem(Orderable):
    block_title = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    info_text = models.TextField(null=True, blank=True)

    panels = [
        FieldPanel('block_title'),
        FieldPanel('address'),
        FieldPanel('phone_number'),
        FieldPanel('email'),
        FieldPanel('info_text'),
    ]

    page = ParentalKey('Footer', related_name='footer_items')

@register_snippet
class Footer(ClusterableModel):
    """The main Footer clustarable model."""
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
        ], heading='Footer'),
        InlinePanel('footer_items', label='Footer Items'),
    ]
    def __str__(self):
        return self.title