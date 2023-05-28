from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from .api_services import get_characters_list, get_comic_by_id, get_comics_list, get_character_by_id, get_creator_by_id, get_event_by_id, get_serie_by_id, get_story_by_id

# HOME


class HomeView(TemplateView):
    template_name = 'homeView.html'
    paginate_by = 2

    # **kargs: any significa que toma cualquier numero de argumentos
    def get_context_data(self, **kwargs):

        context = {
            'title': 'E_Lapse',
            'spider': get_characters_list('spider')
        }
        return context

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('home')

# SEARCH


class SearchView(View):
    template_name = 'searchView.html'

    def get(self, request, *args, **kwargs):
        name_characters = request.GET.get(
            'character_name') or request.session.get('search_query')

        if not name_characters:
            return HttpResponse('No se proporcionó ningún parámetro de búsqueda.')

        characters_list = get_characters_list(name_characters)
        if characters_list is None:
            characters_list = []
        comics_list = get_comics_list(name_characters)
        if comics_list is None:
            comics_list = []

        context = {
            'title': 'E_Lapse',
            'characters': characters_list,
            'comics': comics_list
        }
        return render(request, 'searchView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')


# CHARACTER
class CharacterView(View):
    template_name = 'characterView.html'

    def get(self, request, *args, **kwargs):
        character_id = request.GET.get('character_id')
        character = get_character_by_id(character_id)

        context = {
            'title': 'E_Lapse',
            'characterId': character_id,
            'character': character
        }
        return render(request, 'characterView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')


# COMIC
class ComicView(View):
    template_name = 'comicView.html'

    def get(self, request, *args, **kwargs):
        comic_id = request.GET.get('comic_id')
        comic = get_comic_by_id(comic_id)
        context = {
            'title': 'E_Lapse',
            'comicId': comic_id,
            'comic': comic,
        }
        return render(request, 'comicView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')


# CREATOR
class CreatorView(View):
    template_name = 'creatorView.html'

    def get(self, request, *args, **kwargs):
        creator_id = request.GET.get('creator_id')
        creator = get_creator_by_id(creator_id)
        context = {
            'title': 'E_Lapse',
            'creatorId': creator_id,
            'creator': creator,
        }
        return render(request, 'creatorView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')


# EVENT
class EventView(View):
    template_name = 'eventView.html'

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('event_id')
        event = get_event_by_id(event_id)
        context = {
            'title': 'E_Lapse',
            'eventId': event_id,
            'event': event,
        }
        return render(request, 'eventView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')


# SERIE
class SerieView(View):
    template_name = 'serieView.html'

    def get(self, request, *args, **kwargs):
        serie_id = request.GET.get('serie_id')
        serie = get_serie_by_id(serie_id)
        context = {
            'title': 'E_Lapse',
            'serieId': serie_id,
            'serie': serie,
        }
        return render(request, 'serieView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')


# STORY
class StoryView(View):
    template_name = 'storyView.html'

    def get(self, request, *args, **kwargs):
        story_id = request.GET.get('story_id')
        story = get_story_by_id(story_id)
        context = {
            'title': 'E_Lapse',
            'storyId': story_id,
            'story': story,
        }
        return render(request, 'storyView.html', context)

    def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')

        if name_character:
            return redirect(reverse('search') + f"?character_name={name_character}")
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('search')
