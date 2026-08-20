from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.db.models import Count, Sum
from .models import Article, SiteSettings, UserBan
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

def is_admin(user):
    return user.is_staff or user.is_superuser

def home(request):
    settings = SiteSettings.get_active()
    articles = Article.objects.all()[:5]
    return render(request, 'city/home.html', {'articles': articles, 'settings': settings})

def news(request):
    settings = SiteSettings.get_active()
    articles = Article.objects.all()
    return render(request, 'city/news.html', {'articles': articles, 'settings': settings})

def facts(request):
    settings = SiteSettings.get_active()
    facts_list = [
        {"title": "Зеленоградск — столица кошек", "text": "В городе много скульптур и граффити с кошками."},
        {"title": "Курорт с историей", "text": "Статус курорта город получил еще в XIX веке."},
        {"title": "Балтийское море рядом", "text": "До пляжа можно дойти пешком из центра города."}
    ]
    return render(request, 'city/facts.html', {'facts': facts_list, 'settings': settings})

def contacts(request):
    settings = SiteSettings.get_active()
    contact_info = {
        "address": "г. Зеленоградск, ул. Курортная, д. 1",
        "phone": "+7 (999) 123-45-67",
        "email": "info@zelenogradsk-news.ru",
        "working_hours": "Ежедневно с 09:00 до 18:00"
    }
    return render(request, 'city/contacts.html', {'contact_info': contact_info, 'settings': settings})

def history(request):
    settings = SiteSettings.get_active()
    history_items = [
        {"year": "1816", "event": "Город получил статус курорта"},
        {"year": "1946", "event": "Переименован в Зеленоградск"},
        {"year": "2019", "event": "Открыт променад с видом на море"}
    ]
    return render(request, 'city/history.html', {'history_items': history_items, 'settings': settings})

def history_people(request):
    settings = SiteSettings.get_active()
    people = [
        {"name": "Иван Петров", "role": "Первый городской голова", "years": "1820–1825"},
        {"name": "Мария Сидорова", "role": "Основательница городской библиотеки", "years": "1890–1910"},
        {"name": "Алексей Николаев", "role": "Архитектор променада", "years": "2017–2019"}
    ]
    return render(request, 'city/history_people.html', {'people': people, 'settings': settings})

def history_photos(request):
    settings = SiteSettings.get_active()
    photos = [
        {
            "src": "https://via.placeholder.com/400x300?text=Old+Port",
            "caption": "Старый порт, начало XX века",
            "year": "1905"
        },
        {
            "src": "https://via.placeholder.com/400x300?text=Main+Street",
            "caption": "Центральная улица, 1930-е годы",
            "year": "1932"
        },
        {
            "src": "https://via.placeholder.com/400x300?text=Promenade+Construction",
            "caption": "Строительство променада, наши дни",
            "year": "2018"
        }
    ]
    return render(request, 'city/history_photos.html', {'photos': photos, 'settings': settings})

@user_passes_test(is_admin)
def management(request):
    settings = SiteSettings.get_active()
    
    top_views = Article.objects.order_by('-views')[:5]
    top_saves = Article.objects.order_by('-saves')[:5]

    users = User.objects.all()
    bans = UserBan.objects.filter(is_banned=True)

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'update_styles':
            settings.background_color = request.POST.get('bg_color')
            settings.font_color = request.POST.get('font_color')
            settings.font_size_px = request.POST.get('font_size')
            settings.save()

        elif action == 'ban_user':
            user_id = request.POST.get('user_id')
            duration = request.POST.get('duration')
            reason = request.POST.get('reason')
            user = get_object_or_404(User, id=user_id)
            
            ban, created = UserBan.objects.get_or_create(user=user)
            ban.is_banned = True
            ban.reason = reason
            
            if duration == 'forever':
                ban.banned_until = None
            else:
                days_map = {'day': 1, 'week': 7, 'month': 30}
                ban.banned_until = timezone.now() + timedelta(days=days_map.get(duration, 1))
            
            ban.save()

        elif action == 'unban_user':
            user_id = request.POST.get('user_id')
            user = get_object_or_404(User, id=user_id)
            ban = get_object_or_404(UserBan, user=user)
            ban.is_banned = False
            ban.banned_until = None
            ban.save()

        elif action == 'delete_article':
            article_id = request.POST.get('article_id')
            Article.objects.filter(id=article_id).delete()

        return redirect('management')

    return render(request, 'city/management.html', {
        'settings': settings,
        'top_views': top_views,
        'top_saves': top_saves,
        'users': users,
        'bans': bans
    })

@permission_required('city.add_news', raise_exception=True)
def news_add(request):
    ...

@permission_required('city.change_news', raise_exception=True)
def news_edit(request, pk):
    ...

@permission_required('city.delete_news', raise_exception=True)
def news_delete(request, pk):
    ...






