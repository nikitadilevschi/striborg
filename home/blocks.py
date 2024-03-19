from django.db import models
from wagtail.admin import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.blocks import CharBlock, RichTextBlock, StructBlock, CharBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.snippets.blocks import SnippetChooserBlock
