from django.shortcuts import render

def home(request):
    return render(request, 'city/home.html', {'title': 'Главная — Зеленоградск'})

def news(request):
    return render(request, 'city/news.html', {'title': 'Новости Зеленоградска'})

def management(request):
    return render(request, 'city/management.html', {'title': 'Руководство Зеленоградска'})

def facts(request):
    return render(request, 'city/facts.html', {'title': 'Факты о Зеленоградске'})

def contacts(request):
    return render(request, 'city/contacts.html', {'title': 'Контакты городских служб'})

def history(request):
    return render(request, 'city/history.html', {'title': 'История Зеленоградска'})

def history_people(request):
    return render(request, 'city/history_people.html', {'title': 'Известные жители Зеленоградска'})

def history_photos(request):
    return render(request, 'city/history_photos.html', {'title': 'Исторические фотографии Зеленоградска'})

