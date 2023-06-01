from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from .api_services import get_all_pages, get_attribute_data, get_characters_list, get_comic_by_id, get_comics_list, get_character_by_id, get_creator_by_id, get_creators_list, get_event_by_id, get_serie_by_id, get_story_by_id

# Author: Pablo Barderas Fernández
# Description: Views to render for use on html and provide all data to FRONT-END


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

        # GET CHARACTER NAME
        character_name = request.GET.get(
            'character_name') or request.session.get('search_query')

        # GET CHARACTER PAGE
        character_page = request.GET.get('character_page')

        # GET COMIC PAGE
        comic_page = request.GET.get('comic_page')

        if not character_name:
            return HttpResponse('No se proporcionó ningún parámetro de búsqueda.')

         # Set page to 1 on first search
        if not comic_page:
            return redirect(reverse('search') + f"?character_name={character_name}&character_page=1&comic_page=1")

        # Set page to 1 on first search
        if not character_page:
            return redirect(reverse('search') + f"?character_name={character_name}&character_page=1&comic_page=1")

        # PARSE CHARACTER PAGE TO INT
        try:
            character_page = int(character_page)
            comic_page = int(comic_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            character_page = 1
            comic_page = 1

        # GET ALL CHARACTERS AND COMICS, AND IT'S TOTAL RESULTS FROM SEARCH
        characters_list, total_characters_results = get_characters_list(
            character_name, character_page)
        if characters_list is None:
            characters_list = []
        comics_list, total_comics_results = get_comics_list(
            character_name, comic_page)
        if comics_list is None:
            comics_list = []

        # TODO PAGESSS
        creators_list, total_creators_results = get_creators_list(
            character_name, 1)
        if creators_list is None:
            creators_list = []

        print(creators_list)

        character_pages_range = range(
            1, get_all_pages(total_characters_results)+1)

        comic_pages_range = range(
            1, get_all_pages(total_comics_results)+1)

        # CONTEXT TO FRONT-END
        context = {
            'title': 'E_Lapse',
            'characters': characters_list,
            'character_name': character_name,
            'comics': comics_list,
            'character_page': character_page,
            'comic_page': comic_page,
            'total_characters_results': total_characters_results,
            'total_comics_results': total_comics_results,
            'character_pages_range': character_pages_range,
            'comic_pages_range': comic_pages_range,
            'total_comics_pages': get_all_pages(total_comics_results),
            'total_characters_pages': get_all_pages(total_characters_results),
        }
        return render(request, 'searchView.html', context)


# CHARACTER
class CharacterView(View):
    template_name = 'characterView.html'

    def get(self, request, *args, **kwargs):
        character_id = request.GET.get('character_id')
        character = get_character_by_id(character_id)

        # GET COMIC PAGE
        comic_page = request.GET.get('comic_page')

        # GET EVENT PAGE
        event_page = request.GET.get('event_page')

        # GET SERIE PAGE
        serie_page = request.GET.get('serie_page')

        # GET STORY PAGE
        story_page = request.GET.get('story_page')

        # Set page to 1 on first search
        if not comic_page or not event_page or not serie_page or not story_page:
            return redirect(reverse('character') + f"?character_id={character_id}&comic_page=1&event_page=1&serie_page=1&story_page=1")

        # PARSE PAGES TO INT
        try:
            comic_page = int(comic_page)
            event_page = int(event_page)
            serie_page = int(serie_page)
            story_page = int(story_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            comic_page = 1
            event_page = 1
            serie_page = 1
            story_page = 1

        # GET COMICS, EVENTS, SERIES, STORIES ATRIBUTE, TOTAL RESULTS AND PAGES RANGE
        comics_attribute, total_comics_results, comic_pages_range = Attributes.get_attribute_data(
            character, comic_page, 'comics')
        events_attribute, total_events_results, event_pages_range = Attributes.get_attribute_data(
            character, event_page, 'events')
        series_attribute, total_series_results, serie_pages_range = Attributes.get_attribute_data(
            character, serie_page, 'series')
        stories_attribute, total_stories_results, story_pages_range = Attributes.get_attribute_data(
            character, story_page, 'stories')

        # GET CONTEXT
        context = {
            'title': 'E_Lapse',
            # CHARACTER
            'character_id': character_id,
            'character': character,
            # ATRIBUTES
            'comics_attribute': comics_attribute,
            'events_attribute': events_attribute,
            'series_attribute': series_attribute,
            'stories_attribute': stories_attribute,
            # TOTAL ATRIBUTE RESULTS
            'total_comics_results': total_comics_results,
            'total_events_results': total_events_results,
            'total_series_results': total_series_results,
            'total_stories_results': total_stories_results,
            # ATRIBUTE PAGES
            'comic_page': comic_page,
            'event_page': event_page,
            'serie_page': serie_page,
            'story_page': story_page,
            'comic_pages_range': comic_pages_range,
            'event_pages_range': event_pages_range,
            'serie_pages_range': serie_pages_range,
            'story_pages_range': story_pages_range,
            'total_comics_pages': get_all_pages(total_comics_results),
            'total_events_pages': get_all_pages(total_events_results),
            'total_series_pages': get_all_pages(total_series_results),
            'total_stories_pages': get_all_pages(total_stories_results),
        }
        return render(request, 'characterView.html', context)


# COMIC
class ComicView(View):
    template_name = 'comicView.html'

    def get(self, request, *args, **kwargs):
        comic_id = request.GET.get('comic_id')
        comic = get_comic_by_id(comic_id)

        # GET CHARACTER PAGE
        character_page = request.GET.get('character_page')

        # GET EVENT PAGE
        event_page = request.GET.get('event_page')

        # GET CREATORS PAGE
        creator_page = request.GET.get('creator_page')

        # GET STORY PAGE
        story_page = request.GET.get('story_page')

        # Set page to 1 on first search
        if not character_page or not event_page or not creator_page or not story_page:
            return redirect(reverse('comic') + f"?comic_id={comic_id}&character_page=1&event_page=1&creator_page=1&story_page=1")

        # PARSE PAGES TO INT
        try:
            character_page = int(character_page)
            event_page = int(event_page)
            creator_page = int(creator_page)
            story_page = int(story_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            character_page = 1
            event_page = 1
            creator_page = 1
            story_page = 1

        # GET CHARACTER, EVENTS, CREATORS, STORIES ATRIBUTE, TOTAL RESULTS AND PAGES RANGE
        characters_attribute, total_characters_results, character_pages_range = Attributes.get_attribute_data(
            comic, character_page, 'characters')
        events_attribute, total_events_results, event_pages_range = Attributes.get_attribute_data(
            comic, event_page, 'events')
        creators_attribute, total_creators_results, creator_pages_range = Attributes.get_attribute_data(
            comic, creator_page, 'creators')
        stories_attribute, total_stories_results, story_pages_range = Attributes.get_attribute_data(
            comic, story_page, 'stories')

        context = {
            'title': 'E_Lapse',
            'comicId': comic_id,
            'comic': comic,
            # ATRIBUTES
            'characters_attribute': characters_attribute,
            'events_attribute': events_attribute,
            'creators_attribute': creators_attribute,
            'stories_attribute': stories_attribute,
            # TOTAL ATRIBUTE RESULTS
            'total_characters_results': total_characters_results,
            'total_events_results': total_events_results,
            'total_creators_results': total_creators_results,
            'total_stories_results': total_stories_results,
            # ATRIBUTE PAGES
            'character_page': character_page,
            'event_page': event_page,
            'creator_page': creator_page,
            'story_page': story_page,
            'character_pages_range': character_pages_range,
            'event_pages_range': event_pages_range,
            'creator_pages_range': creator_pages_range,
            'story_pages_range': story_pages_range,
            'total_characters_pages': get_all_pages(total_characters_results),
            'total_events_pages': get_all_pages(total_events_results),
            'total_creators_pages': get_all_pages(total_creators_results),
            'total_stories_pages': get_all_pages(total_stories_results),
        }
        return render(request, 'comicView.html', context)


# CREATOR
class CreatorView(View):
    template_name = 'creatorView.html'

    def get(self, request, *args, **kwargs):
        creator_id = request.GET.get('creator_id')
        creator = get_creator_by_id(creator_id)

        # GET COMIC PAGE
        comic_page = request.GET.get('comic_page')

        # GET EVENT PAGE
        event_page = request.GET.get('event_page')

        # GET SERIE PAGE
        serie_page = request.GET.get('serie_page')

        # GET STORY PAGE
        story_page = request.GET.get('story_page')

        # Set page to 1 on first search
        if not comic_page or not event_page or not serie_page or not story_page:
            return redirect(reverse('creator') + f"?creator_id={creator_id}&comic_page=1&event_page=1&serie_page=1&story_page=1")

        # PARSE PAGES TO INT
        try:
            comic_page = int(comic_page)
            event_page = int(event_page)
            serie_page = int(serie_page)
            story_page = int(story_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            comic_page = 1
            event_page = 1
            serie_page = 1
            story_page = 1

        # GET COMICS, EVENTS, SERIES, STORIES ATRIBUTE, TOTAL RESULTS AND PAGES RANGE
        comics_attribute, total_comics_results, comic_pages_range = Attributes.get_attribute_data(
            creator, comic_page, 'comics')
        events_attribute, total_events_results, event_pages_range = Attributes.get_attribute_data(
            creator, event_page, 'events')
        series_attribute, total_series_results, serie_pages_range = Attributes.get_attribute_data(
            creator, serie_page, 'series')
        stories_attribute, total_stories_results, story_pages_range = Attributes.get_attribute_data(
            creator, 1, 'stories')

        context = {
            'title': 'E_Lapse',
            'creatorId': creator_id,
            'creator': creator,
            # ATRIBUTES
            'comics_attribute': comics_attribute,
            'events_attribute': events_attribute,
            'series_attribute': series_attribute,
            'stories_attribute': stories_attribute,
            # TOTAL ATRIBUTE RESULTS
            'total_comics_results': total_comics_results,
            'total_events_results': total_events_results,
            'total_series_results': total_series_results,
            'total_stories_results': total_stories_results,
            # ATRIBUTE PAGES
            'comic_page': comic_page,
            'event_page': event_page,
            'serie_page': serie_page,
            'story_page': story_page,
            'comic_pages_range': comic_pages_range,
            'event_pages_range': event_pages_range,
            'serie_pages_range': serie_pages_range,
            'story_pages_range': story_pages_range,
            'total_comics_pages': get_all_pages(total_comics_results),
            'total_events_pages': get_all_pages(total_events_results),
            'total_series_pages': get_all_pages(total_series_results),
            'total_stories_pages': get_all_pages(total_stories_results),
        }
        return render(request, 'creatorView.html', context)


# EVENT
class EventView(View):
    template_name = 'eventView.html'

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('event_id')
        event = get_event_by_id(event_id)

        # GET COMIC PAGE
        comic_page = request.GET.get('comic_page')

        # GET CHARACTER PAGE
        character_page = request.GET.get('character_page')

        # GET SERIE PAGE
        serie_page = request.GET.get('serie_page')

        # GET STORY PAGE
        story_page = request.GET.get('story_page')

        # GET CREATORS PAGE
        creator_page = request.GET.get('creator_page')

        # Set page to 1 on first search
        if not comic_page or not character_page or not serie_page or not story_page or not creator_page:
            return redirect(reverse('event') + f"?event_id={event_id}&comic_page=1&character_page=1&creator_page=1&serie_page=1&story_page=1")

        # PARSE PAGES TO INT
        try:
            comic_page = int(comic_page)
            character_page = int(character_page)
            serie_page = int(serie_page)
            story_page = int(story_page)
            creator_page = int(creator_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            comic_page = 1
            character_page = 1
            serie_page = 1
            story_page = 1
            creator_page = 1

        # GET COMICS, CHARACTERS, SERIES, STORIES, CREATORS ATRIBUTE, TOTAL RESULTS AND PAGES RANGE
        comics_attribute, total_comics_results, comic_pages_range = Attributes.get_attribute_data(
            event, comic_page, 'comics')
        characters_attribute, total_characters_results, character_pages_range = Attributes.get_attribute_data(
            event, character_page, 'characters')
        series_attribute, total_series_results, serie_pages_range = Attributes.get_attribute_data(
            event, serie_page, 'series')
        stories_attribute, total_stories_results, story_pages_range = Attributes.get_attribute_data(
            event, story_page, 'stories')
        creators_attribute, total_creators_results, creator_pages_range = Attributes.get_attribute_data(
            event, creator_page, 'creators')

        context = {
            'title': 'E_Lapse',
            'eventId': event_id,
            'event': event,
            # ATRIBUTES
            'comics_attribute': comics_attribute,
            'characters_attribute': characters_attribute,
            'series_attribute': series_attribute,
            'stories_attribute': stories_attribute,
            'creators_attribute': creators_attribute,
            # TOTAL ATRIBUTE RESULTS
            'total_comics_results': total_comics_results,
            'total_characters_results': total_characters_results,
            'total_series_results': total_series_results,
            'total_stories_results': total_stories_results,
            'total_creators_results': total_creators_results,
            # ATRIBUTE PAGES
            'comic_page': comic_page,
            'character_page': character_page,
            'serie_page': serie_page,
            'story_page': story_page,
            'creator_page': creator_page,
            'comic_pages_range': comic_pages_range,
            'character_pages_range': character_pages_range,
            'serie_pages_range': serie_pages_range,
            'story_pages_range': story_pages_range,
            'creator_pages_range': creator_pages_range,
            'total_comics_pages': get_all_pages(total_comics_results),
            'total_characters_pages': get_all_pages(total_characters_results),
            'total_series_pages': get_all_pages(total_series_results),
            'total_stories_pages': get_all_pages(total_stories_results),
            'total_creators_pages': get_all_pages(total_creators_results),
        }
        return render(request, 'eventView.html', context)


# SERIE
class SerieView(View):
    template_name = 'serieView.html'

    def get(self, request, *args, **kwargs):
        serie_id = request.GET.get('serie_id')
        serie = get_serie_by_id(serie_id)

        # GET COMIC PAGE
        comic_page = request.GET.get('comic_page')

        # GET CHARACTER PAGE
        character_page = request.GET.get('character_page')

        # GET EVENT PAGE
        event_page = request.GET.get('event_page')

        # GET STORY PAGE
        story_page = request.GET.get('story_page')

        # GET CREATORS PAGE
        creator_page = request.GET.get('creator_page')

        # Set page to 1 on first search
        if not comic_page or not character_page or not event_page or not story_page or not creator_page:
            return redirect(reverse('serie') + f"?serie_id={serie_id}&comic_page=1&character_page=1&creator_page=1&event_page=1&story_page=1")

        # PARSE PAGES TO INT
        try:
            comic_page = int(comic_page)
            character_page = int(character_page)
            event_page = int(event_page)
            story_page = int(story_page)
            creator_page = int(creator_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            comic_page = 1
            character_page = 1
            event_page = 1
            story_page = 1
            creator_page = 1

         # GET COMICS, CHARACTERS, SERIES, STORIES, CREATORS ATRIBUTE, TOTAL RESULTS AND PAGES RANGE
        comics_attribute, total_comics_results, comic_pages_range = Attributes.get_attribute_data(
            serie, comic_page, 'comics')
        characters_attribute, total_characters_results, character_pages_range = Attributes.get_attribute_data(
            serie, character_page, 'characters')
        events_attribute, total_events_results, event_pages_range = Attributes.get_attribute_data(
            serie, event_page, 'events')
        stories_attribute, total_stories_results, story_pages_range = Attributes.get_attribute_data(
            serie, story_page, 'stories')
        creators_attribute, total_creators_results, creator_pages_range = Attributes.get_attribute_data(
            serie, creator_page, 'creators')

        context = {
            'title': 'E_Lapse',
            'serieId': serie_id,
            'serie': serie,
            # ATRIBUTES
            'comics_attribute': comics_attribute,
            'characters_attribute': characters_attribute,
            'events_attribute': events_attribute,
            'stories_attribute': stories_attribute,
            'creators_attribute': creators_attribute,
            # TOTAL ATRIBUTE RESULTS
            'total_comics_results': total_comics_results,
            'total_characters_results': total_characters_results,
            'total_events_results': total_events_results,
            'total_stories_results': total_stories_results,
            'total_creators_results': total_creators_results,
            # ATRIBUTE PAGES
            'comic_page': comic_page,
            'character_page': character_page,
            'event_page': event_page,
            'story_page': story_page,
            'creator_page': creator_page,
            'comic_pages_range': comic_pages_range,
            'character_pages_range': character_pages_range,
            'event_pages_range': event_pages_range,
            'story_pages_range': story_pages_range,
            'creator_pages_range': creator_pages_range,
            'total_comics_pages': get_all_pages(total_comics_results),
            'total_characters_pages': get_all_pages(total_characters_results),
            'total_events_pages': get_all_pages(total_events_results),
            'total_stories_pages': get_all_pages(total_stories_results),
            'total_creators_pages': get_all_pages(total_creators_results),
        }
        return render(request, 'serieView.html', context)


# STORY
class StoryView(View):
    template_name = 'storyView.html'

    def get(self, request, *args, **kwargs):
        story_id = request.GET.get('story_id')
        story = get_story_by_id(story_id)

        # GET COMIC PAGE
        comic_page = request.GET.get('comic_page')

        # GET CHARACTER PAGE
        character_page = request.GET.get('character_page')

        # GET EVENT PAGE
        event_page = request.GET.get('event_page')

        # GET SERIE PAGE
        serie_page = request.GET.get('serie_page')

        # GET CREATORS PAGE
        creator_page = request.GET.get('creator_page')

        # Set page to 1 on first search
        if not comic_page or not character_page or not serie_page or not creator_page or not event_page:
            return redirect(reverse('story') + f"?story_id={story_id}&comic_page=1&character_page=1&creator_page=1&serie_page=1&event_page=1")

        # PARSE PAGES TO INT
        try:
            comic_page = int(comic_page)
            character_page = int(character_page)
            serie_page = int(serie_page)
            event_page = int(event_page)
            creator_page = int(creator_page)
        except (TypeError, ValueError):
            # If unable to convert to number, set default page value to 1
            comic_page = 1
            character_page = 1
            serie_page = 1
            event_page = 1
            creator_page = 1

        # GET COMICS, CHARACTERS, SERIES, EVENTS, CREATORS ATRIBUTE, TOTAL RESULTS AND PAGES RANGE
        comics_attribute, total_comics_results, comic_pages_range = Attributes.get_attribute_data(
            story, comic_page, 'comics')
        characters_attribute, total_characters_results, character_pages_range = Attributes.get_attribute_data(
            story, character_page, 'characters')
        series_attribute, total_series_results, serie_pages_range = Attributes.get_attribute_data(
            story, serie_page, 'series')
        events_attribute, total_events_results, event_pages_range = Attributes.get_attribute_data(
            story, event_page, 'events')
        creators_attribute, total_creators_results, creator_pages_range = Attributes.get_attribute_data(
            story, creator_page, 'creators')

        context = {
            'title': 'E_Lapse',
            'storyId': story_id,
            'story': story,
            # ATRIBUTES
            'comics_attribute': comics_attribute,
            'characters_attribute': characters_attribute,
            'series_attribute': series_attribute,
            'events_attribute': events_attribute,
            'creators_attribute': creators_attribute,
            # TOTAL ATRIBUTE RESULTS
            'total_comics_results': total_comics_results,
            'total_characters_results': total_characters_results,
            'total_series_results': total_series_results,
            'total_events_results': total_events_results,
            'total_creators_results': total_creators_results,
            # ATRIBUTE PAGES
            'comic_page': comic_page,
            'character_page': character_page,
            'serie_page': serie_page,
            'event_page': event_page,
            'creator_page': creator_page,
            'comic_pages_range': comic_pages_range,
            'character_pages_range': character_pages_range,
            'serie_pages_range': serie_pages_range,
            'event_pages_range': event_pages_range,
            'creator_pages_range': creator_pages_range,
            'total_comics_pages': get_all_pages(total_comics_results),
            'total_characters_pages': get_all_pages(total_characters_results),
            'total_series_pages': get_all_pages(total_series_results),
            'total_events_pages': get_all_pages(total_events_results),
            'total_creators_pages': get_all_pages(total_creators_results),
        }

        print(comic_page)
        return render(request, 'storyView.html', context)


# GET ATRIBUTES
class Attributes():

    # GET DATA OF SPECIFIC ATRIBUTE
    def get_attribute_data(entity, page, type_attribute):
        attribute_list = []
        for attribute in entity:
            total_entity_results = attribute[type_attribute]['available']
        attribute_list.append(
            get_attribute_data(attribute[type_attribute]['collectionURI'], page))

        comic_pages_range = range(
            1, get_all_pages(total_entity_results)+1)

        return attribute_list, total_entity_results, comic_pages_range
