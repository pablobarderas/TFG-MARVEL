from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from .api_services import get_characters_list, get_comics_list


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
            return redirect(reverse('search', kwargs={'character': name_character}))
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('home')


class SearchView(View):
    template_name = 'searchView.html'

    def get(self, request, *args, **kwargs):
        name_character = kwargs.get(
            'character') or request.session.get('search_query')

        if not name_character:
            return HttpResponse('No se proporcionó ningún parámetro de búsqueda.')

        characters_list = get_characters_list(name_character)
        if characters_list is None:
            characters_list = []
        comics_list = get_comics_list(name_character)
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
            request.session['search_query'] = name_character
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
        return redirect('search')

    # Los comento, porque no se como direccionarlos


class CharacterView(View):
    template_name = 'characterView.html'

    def get(self, request, *args, **kwargs):
        name_character = kwargs.get(
            'character')

        characters_list = get_characters_list(name_character)
        if characters_list is None:
            characters_list = []
        comics_list = get_comics_list(name_character)
        if comics_list is None:
            comics_list = []

        context = {
            'title': 'E_Lapse',
            'characters': characters_list,
            'comics': comics_list
        }
        return render(request, 'characterView.html', context)

# class ComicView(View):
#     template_name = 'comicView.html'
#     paginate_by = 2

# class CreatorView(View):
#     template_name = 'creatorView.html'
#     paginate_by = 2

# class EventView(View):
#     template_name = 'eventView.html'
#     paginate_by = 2

# class SerieView(View):
#     template_name = 'serieView.html'
#     paginate_by = 2

# class CreatorView(View):
#     template_name = 'creatorView.html'
#     paginate_by = 2
