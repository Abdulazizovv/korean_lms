from django.contrib import admin
from .models import BotUser


class BotUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'first_name', 'last_name', 'phone_number', 'language_code', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('user_id', 'username', 'first_name', 'last_name', 'phone_number', 'language_code')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(BotUser, BotUserAdmin)
