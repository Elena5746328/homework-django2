from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SiteSettings(models.Model):
    background_color = models.CharField(max_length=7, default="#ffffff")
    font_color = models.CharField(max_length=7, default="#333333")
    font_size_px = models.PositiveIntegerField(default=16)

    @classmethod
    def get_active(cls):
        obj = cls.objects.first()
        if not obj:
            obj = cls.objects.create()
        return obj

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст статьи")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    saves = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class UserBan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ban_info")
    is_banned = models.BooleanField(default=False)
    banned_until = models.DateTimeField(null=True, blank=True)
    reason = models.TextField(blank=True)

    def is_active(self):
        if not self.is_banned:
            return False
        if self.banned_until and self.banned_until < timezone.now():
            self.is_banned = False
            self.save()
            return False
        return True

