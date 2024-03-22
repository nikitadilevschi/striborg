from django.db import models

from wagtail.models import Page, ParentalKey, Orderable, Site
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField

from wagtail.blocks import CharBlock, RichTextBlock, StructBlock, CharBlock, TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from home import blocks

class HomePageCarouselImages(Orderable):
    """Between 1 and 3 images for the home page carousel."""


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
    body = StreamField([
        ('rtfblock', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
        ('cards', blocks.CardBlock()),
        ('about_us_blocks', blocks.AboutUsBlock()),
    ],
        null=True, blank=True)

    #Interface admin fields
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=3, min_num=1, label="Carousel"),
        ]),
        MultiFieldPanel([
            FieldPanel('body'),
        ])
    ]

class OurServices(Page):

    template = "home/our_services.html"

    def get_context(self, request):
        context = super().get_context(request)
        home_page = HomePage.objects.first()
        if home_page:
            context['cards'] = [block for block in home_page.body if isinstance(block.block, blocks.CardBlock)]
        else:
            print("HomePage not found")
        return context


class AboutUs(Page):

    template = "home/about_us.html"

    def get_context(self, request):
        context = super().get_context(request)
        home_page = HomePage.objects.first()
        if home_page:
            context['about_us_blocks'] = [block for block in home_page.body if isinstance(block.block, blocks.AboutUsBlock)]
        else:
            print("HomePage not found")
        return context