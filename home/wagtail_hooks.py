from wagtail_modeladmin.options import (
    ModelAdmin, modeladmin_register)
from django.contrib.auth.models import User

class UserAdmin(ModelAdmin):
    model = User
    menu_label = 'Users'
    menu_icon = 'user'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('username', 'email', 'is_active')  # Make sure 'is_active' is included here
    list_filter = ('is_active',)
    search_fields = ('username', 'email')

modeladmin_register(UserAdmin)