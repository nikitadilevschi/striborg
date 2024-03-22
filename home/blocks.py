from django.db import models
from wagtail.admin import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock

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
    about_description = blocks.TextBlock(required=True, help_text='Description of the about us section')
    button_page = blocks.PageChooserBlock(required=False, help_text='Link to internal page')
    image = ImageChooserBlock(required=True, help_text='Image of the section')

    class Meta:
        template = 'about_us_block.html'
        icon = 'placeholder'
        label = 'About Us'