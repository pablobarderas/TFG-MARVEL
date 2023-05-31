import hashlib
import math
import requests
import json


# GET JSON DATA OF ATRIBUTES BY URI
def get_atribute_data(url, page):
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 21,
        'offset': 0
    }
    args = page_selected(args, page)
    # print(args)
    data, total_results, page = get_data_list(url, args, page)
    return data


# GET DATA BY ENDPOINT
def get_data(endpoint, params, page):
    BASE_URL = "https://gateway.marvel.com/v1/public/"
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 21,
        'offset': 0
    }
    args.update(params)

    args = page_selected(args, page)

    url = BASE_URL + endpoint
    list, total_results, page = get_data_list(url, args, page)
    return list, total_results, page


def get_characters_list(nameStartsWith, page):
    endpoint = "characters"
    params = {'nameStartsWith': nameStartsWith}
    characters, total_results, page = get_data(endpoint, params, page)
    return characters, total_results


def get_comics_list(titleStartsWith, page):
    endpoint = "comics"
    params = {'titleStartsWith': titleStartsWith}
    comics, total_results, page = get_data(endpoint, params, page)
    return comics, total_results


def get_creators_list(nameStartsWith):
    endpoint = "creators"
    params = {'nameStartsWith': nameStartsWith}
    creators, total_results, page = get_data(endpoint, params, page)
    return get_data(endpoint, params)


def get_events_list(nameStartsWith):
    endpoint = "events"
    params = {'nameStartsWith': nameStartsWith}
    events, total_results, page = get_data(endpoint, params, page)
    return events, total_results


def get_series_list(titleStartsWith, page):
    endpoint = "series"
    params = {'titleStartsWith': titleStartsWith}
    series, total_results, page = get_data(endpoint, params, page)
    return series, total_results


def get_story_by_id(story_id):
    endpoint = "stories/" + story_id
    story, args, page = get_data(endpoint, {}, 0)
    return story


def get_serie_by_id(serie_id):
    endpoint = "series/" + serie_id
    serie, args, page = get_data(endpoint, {}, 0)
    return serie


def get_event_by_id(event_id):
    endpoint = "events/" + event_id
    event, args, page = get_data(endpoint, {}, 0)
    return event


def get_creator_by_id(creator_id):
    endpoint = "creators/" + creator_id
    creator, args, page = get_data(endpoint, {}, 0)
    return creator


def get_character_by_id(character_id):
    endpoint = "characters/" + character_id
    character, args, page = get_data(endpoint, {}, 0)
    return character


def get_comic_by_id(comic_id):
    endpoint = "comics/" + comic_id
    comic, args, page = get_data(endpoint, {}, 0)
    return comic


# GET DATA LIST RESPONSE AND PARSE JSON
def get_data_list(url, args, page):
    data_list = []
    response = requests.get(url, params=args)

    # PARSE JSON TO DICTIONARY
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        for json_element in responseJson['data']['results']:
            data_list.append(json_element)

        # GET TOTAL RESULTS OF THIS REQUEST
        total_results = responseJson['data']['total']

    return data_list, total_results, page


# GET ALL PAGES BY TOTAL RESULTS
def get_all_pages(total_results):
    return math.ceil(total_results/21)


# OFFSET BY PAGE SELECTED
def page_selected(args, page):
    offset = (page - 1) * 21
    # PAGINATION
    if (page > 1):
        args.update({'offset': offset})
    return args


# GET HASH OF URL
def getHash(ts):

    # CLAVES Y HASH NECESARIOS PARA LA PETICION
    publicKey = 'dbc203265f84033afd469a493cec6b27'
    privateKey = '1bd9e9686369a65ff11aa1e51919e884ad04765f'
    preHash = str(ts) + privateKey + publicKey
    # SE USA .encode PORQUE preHash ES UN STRING
    hash = hashlib.md5(preHash.encode()).hexdigest()
    return hash
