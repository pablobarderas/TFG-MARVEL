from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from .api_services import get_all_pages, get_characters_list, get_comic_by_id, get_comics_list, get_character_by_id, get_creator_by_id, get_event_by_id, get_serie_by_id, get_story_by_id

# HOME


class HomeView(TemplateView):
    template_name = 'homeView.html'

    # **kargs: any significa que toma cualquier numero de argumentos
    def get_context_data(self, **kwargs):

        context = {
            'title': 'E_Lapse',
        }
        return context

    def get(self, request, *args, **kwargs):

        if request.method == 'GET' and 'character_name' in request.GET:
            character_name = request.GET['character_name']
            return redirect(reverse('search') + f"?character_name={character_name}")

        return super().get(request, *args, **kwargs)


# SEARCH


class SearchView(View):
    template_name = 'searchView.html'

    def get(self, request, *args, **kwargs):
        character_name = request.GET.get(
            'character_name') or request.session.get('search_query')
        page = request.GET.get('page')
        if not character_name:
            return HttpResponse('No se proporcionó ningún parámetro de búsqueda.')

        # GET ALL CHARACTERS AND COMICS, AND IT'S TOTAL RESULTS FROM SEARCH
        page = 1
        characters_list, total_characters_results = get_characters_list(
            character_name, page)
        if characters_list is None:
            characters_list = []
        comics_list, total_comics_results = get_comics_list(
            character_name, page)
        if comics_list is None:
            comics_list = []

        print("Total comics:", total_comics_results,
              "Total comics pages:", get_all_pages(total_comics_results))
        print("Total characters:", total_characters_results,
              "Total characters pages:", get_all_pages(total_characters_results))

        # CONTEXT TO FRONT-END
        context = {
            'title': 'E_Lapse',
            'characters': characters_list,
            'character_name': character_name,
            'comics': comics_list,
            'total_characters_results': total_characters_results,
            'total_comics_results': total_comics_results,
            'total_characters_pages': get_all_pages(total_characters_results),
            'total_comics_pages': get_all_pages(total_comics_results),
        }
        return render(request, 'searchView.html', context)

    # def post(self, request, *args, **kwargs):
        name_character = request.POST.get('nameCharacter')
        page = request.GET.get("page")

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


# LISTENER FOR SEARCH BY NAVEGATION BAR
def search_by_name(self, request, *args, **kwargs):
    name_character = request.GET.get('nameCharacter')

    if name_character:
        return redirect(reverse('search') + f"?character_name={name_character}")
    else:
        messages.error(
            request, 'No se proporcionó ningún parámetro de búsqueda.')
        return redirect('search')
