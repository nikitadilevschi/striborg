from django.db import models

from wagtail.models import Page, ParentalKey, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField

from wagtail.blocks import CharBlock, RichTextBlock, StructBlock, CharBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.snippets.blocks import SnippetChooserBlock



@register_snippet
class Header(models.Model):

    bodytext = RichTextField()

    panels = [
        FieldPanel('bodytext'),
    ]
    def __str__(self):
        return self.bodytext


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel("carousel_image"),
        FieldPanel("title"),
        FieldPanel("description"),
    ]


class HomePage(Page):

    template = "home/home_page.html"
    max_count = 1

    # Database fields
    subtitle = models.CharField(max_length=100,
                                blank=True,
                                null=True)

    rtfbody = RichTextField(blank=True, null=True)

    body = StreamField([
        ('rtfblock', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
    ],
        null=True, blank=True)

    #Interface admin fields
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, min_num=1, label="Carousel"),
        ]),
        MultiFieldPanel([
            FieldPanel('subtitle'),
            FieldPanel('rtfbody'),
            FieldPanel('body'),
        ])
    ]

class ServicePage(Page):
    body = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


