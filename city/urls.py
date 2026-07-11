from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<path:subpath>/', views.news, name='news_catchall'),
    path('management/', views.management, name='management'),
    path('management/<path:subpath>/', views.management, name='management_catchall'),
    path('facts/', views.facts, name='facts'),
    path('facts/<path:subpath>/', views.facts, name='facts_catchall'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<path:subpath>/', views.contacts, name='contacts_catchall'),
    path('history/', views.history, name='history'),
    path('history/people/', views.history_people, name='history_people'),
    path('history/photos/', views.history_photos, name='history_photos'),
]


