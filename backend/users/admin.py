from django.contrib import admin
from .models import User, Profile, OneTimeCode


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','phone_number', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
    search_fields = ['phone_number', 'first_name', 'last_name', 'email']
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    ordering = ['phone_number']
    filter_horizontal = ()
    list_display_links = ['phone_number', 'first_name', 'last_name', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'username', 'bio', 'image', 'created_at', 'updated_at']
    search_fields = ['user', 'username', 'bio']
    list_filter = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('user', 'username', 'bio', 'image')}),
    )
    ordering = ['user']
    filter_horizontal = ()
    list_display_links = ['user', 'username', 'bio', 'image']


class OneTimeCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created_at', 'updated_at', 'is_used']
    search_fields = ['user', 'code']
    list_filter = ['created_at', 'updated_at', 'is_used']
    fieldsets = (
        (None, {'fields': ('user', 'code', 'is_used')}),
    )
    ordering = ['user']
    filter_horizontal = ()
    list_display_links = ['user', 'code', 'is_used']


admin.site.register(OneTimeCode, OneTimeCodeAdmin)


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
