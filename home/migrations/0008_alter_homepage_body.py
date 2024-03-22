# Generated by Django 5.0.3 on 2024-03-22 10:15

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_aboutus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('rtfblock', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('cards', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Title of the section', required=True)), ('section_description', wagtail.blocks.TextBlock(help_text='Description of the section', required=True)), ('section_button', wagtail.blocks.PageChooserBlock(help_text='Link to internal page', required=False)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(help_text='Icon Image', required=True)), ('card_title', wagtail.blocks.CharBlock(help_text='Title of the card', required=True)), ('card_description', wagtail.blocks.TextBlock(help_text='Description of the card', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Link to internal page', required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='Link to a external URL', required=False))])))])), ('about_us_blocks', wagtail.blocks.StructBlock([('block_title', wagtail.blocks.CharBlock(help_text='Title of the section', required=True)), ('block_description', wagtail.blocks.TextBlock(help_text='Description of the section', required=True)), ('about_title', wagtail.blocks.CharBlock(help_text='Title of the about us section', required=True)), ('about_description', wagtail.blocks.TextBlock(help_text='Description of the about us section', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image of the section', required=True))]))], blank=True, null=True),
        ),
    ]