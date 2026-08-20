from django.contrib import admin
from .models import Article, SiteSettings, UserBan

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views', 'saves')
    search_fields = ('title', 'content')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('background_color', 'font_color', 'font_size_px')

@admin.register(UserBan)
class UserBanAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_banned', 'banned_until', 'reason')
    list_filter = ('is_banned',)




