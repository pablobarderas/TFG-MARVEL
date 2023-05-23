from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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
            request.session['search_query'] = name_character
            return redirect('search')
        else:
            messages.error(
                request, 'No se proporcionó ningún parámetro de búsqueda.')
            return redirect('home')


class SearchView(View):
    template_name = 'searchView.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        name_character = request.session.get('search_query')

        if not name_character:
            return HttpResponse('No se proporcionó ningún parámetro de búsqueda.')

        characters_list = get_characters_list(name_character)
        if characters_list is None:
            characters_list = []
        comics_list = get_comics_list(name_character)
        if comics_list is None:
            comics_list = []

        # Configuración de la paginación
        # Mostrar 10 personajes por página
        characters_paginator = Paginator(characters_list, 4)
        # Mostrar 5 cómics por página
        comics_paginator = Paginator(comics_list, 5)

        # Obtener el número de página solicitada (por defecto es la primera página)
        characters_page_number = request.GET.get('characters_page')
        comics_page_number = request.GET.get('comics_page')

        # Obtener las páginas solicitadas
        characters_page = characters_paginator.get_page(characters_page_number)
        comics_page = comics_paginator.get_page(comics_page_number)

        context = {
            'title': 'E_Lapse',
            'characters': characters_page,
            'comics': comics_page
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
# class CharacterView(View):
#     template_name = 'characterView.html'
#     paginate_by = 2

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
