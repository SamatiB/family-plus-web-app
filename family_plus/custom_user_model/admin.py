from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_user_model.models import CustomUserModel


class CustomAdmin(UserAdmin):

    """Custom admin set up for the custom user model."""

    list_display = ('email', 'username', 'date_joined', 'last_login',
                    'is_admin', 'is_staff')
    search_fields = ('email', 'usermame')
    readonly_fields = ('id', 'date_joined', 'last_login')

    # Turn off filters
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()


admin.site.register(CustomUserModel, CustomAdmin)