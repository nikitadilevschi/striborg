from bs4 import BeautifulSoup
from django.db import models
from wagtail.admin import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
import feedparser
from dateutil.parser import parse

class CardBlock(blocks.StructBlock):
    """Card With Icons and Text Block"""
    section_title = blocks.CharBlock(required=True, help_text='Title of the section')
    section_description = blocks.TextBlock(required=True, help_text='Description of the section')
    section_button = blocks.PageChooserBlock(required=False, help_text='Link to internal page')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('icon', ImageChooserBlock(required=True, help_text='Icon Image')),
                ('card_title', blocks.CharBlock(required=True, help_text='Title of the card')),
                ('card_description', blocks.TextBlock(required=True, help_text='Description of the card')),
                ("button_page", blocks.PageChooserBlock(required=False, help_text='Link to internal page')),
                ("button_url", blocks.URLBlock(required=False, help_text='Link to a external URL')),
            ]
        )
    )

    class Meta:
        template = 'card_block.html'
        icon = 'placeholder'
        label = 'Our Services'

class AboutUsBlock(blocks.StructBlock):
    """About Us Block"""
    block_title = blocks.CharBlock(required=True, help_text='Title of the section')
    block_description = blocks.TextBlock(required=True, help_text='Description of the section')
    about_title = blocks.CharBlock(required=True, help_text='Title of the about us section')
    about_description = blocks.RichTextBlock(required=True, help_text='Description of the about us section')
    button_page = blocks.PageChooserBlock(required=False, help_text='Link to internal page')
    image = ImageChooserBlock(required=True, help_text='Image of the section')

    class Meta:
        template = 'about_us_block.html'
        icon = 'placeholder'
        label = 'About Us'

class MarketOverviewBlock(blocks.StructBlock):
    """Market Overview Block"""

    block_title = blocks.CharBlock(required=True, help_text='Title of the section')
    button_page = blocks.PageChooserBlock(required=False, help_text='Link to internal page')

    class Meta:
        template = 'market_overview_block.html'
        icon = 'placeholder'
        label = 'Market Overview'


class RSSFeedBlock(blocks.StructBlock):
    block_title = blocks.CharBlock(required=True, help_text='Title of the section')
    feed_url = blocks.CharBlock(required=True, help_text="Enter the URL of the RSS feed you want to display")
    count = blocks.CharBlock(required=True, help_text="Enter the number of items you want to display")

    class Meta:
        template = "feed_block.html"
        icon = "fa-rss"
        label = "RSS Feed"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        feed = feedparser.parse(value['feed_url'])
        for entry in feed.entries:
            soup = BeautifulSoup(entry.description, 'html.parser')
            entry['image_url'] = soup.img['src'] if soup.img else None
            entry['description'] = soup.get_text()
        # sort the entries by publication date in descending order
        feed.entries.sort(key=lambda x: x.published_parsed, reverse=True)
        context['feed'] = feed.entries[:int(value['count'])]
        return context