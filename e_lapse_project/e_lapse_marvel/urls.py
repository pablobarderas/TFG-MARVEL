from django.contrib import admin
from django.urls import path
from .views import CreatorView, HomeView, SearchView, CharacterView, ComicView, EventView, StoryView, SerieView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),

    path('character/', CharacterView.as_view(), name='character'),
    path('comic/', ComicView.as_view(), name='comic'),
    path('creator/', CreatorView.as_view(), name='creator'),
    path('event/', EventView.as_view(), name='event'),
    path('story/', StoryView.as_view(), name='story'),
    path('serie/', SerieView.as_view(), name='serie')
]
