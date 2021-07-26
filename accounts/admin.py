from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import State, UserData, UserDocuments, PremiumUser


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('name', 'email', 'phone', 'type', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('name', 'email', 'type', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

class UserDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'state', 'city']

class UserDocumentsAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(UserData, UserDataAdmin)
admin.site.register(UserDocuments, UserDocumentsAdmin)
admin.site.register(PremiumUser)
