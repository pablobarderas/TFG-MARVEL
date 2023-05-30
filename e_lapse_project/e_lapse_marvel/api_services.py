import hashlib
import requests
import json


'''
        # Get count of total results and request results
        totalResults = responseJson['data']['total']
        totalCount = responseJson['data']['count']
        # IF THERE ARE COMICS LEFT TO PICK UP
        while totalCount < totalResults:
            # Actualizar el offset en cada iteración
            args['offset'] += 100
            responseRest = requests.get(BASE_URL, params=args)
            responseJsonRest = json.loads(responseRest.text)

            print("*******Total results:", totalResults,
                  "\n*******Total count:", totalCount)

            # ADD REST OF CHARACTERS
            for character in responseJsonRest['data']['results']:
                character_list.append(character)
            totalCount += responseJsonRest['data']['count']
'''
'''
    response = requests.get(BASE_URL, params=args)
    # SI LA RESPUESTA ES CORRECTA, SE GUARDA UNA LISTA CON TODOS LOS PERSONAJES
    if (response.status_code == 200):
        responseJson = json.loads(response.text)
        comics_list = getJsonList(responseJson)

        # Get count of total results and request results
        totalResults = responseJson['data']['total']
        totalCount = responseJson['data']['count']

        # IF THERE ARE COMICS LEFT TO PICK UP
        
        while totalCount < totalResults:
            # Actualizar el offset en cada iteración
            args['offset'] += 100
            responseRest = requests.get(BASE_URL, params=args)
            responseJsonRest = json.loads(responseRest.text)

            print("*******Total comics results:", totalResults,
                  "\n*******Total comics count:", totalCount)

            # ADD REST OF CHARACTERS
            for comic in responseJsonRest['data']['results']:
                comics_list.append(comic)
            totalCount += responseJsonRest['data']['count']
'''


def get_data(endpoint, params):
    BASE_URL = "https://gateway.marvel.com/v1/public/"
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 20,
        'offset': 0
    }
    args.update(params)
    url = BASE_URL + endpoint
    page = 0
    list, total_results, page = get_data_list(url, args, page)
    print(total_results)
    return list, total_results


def get_characters_list(nameStartsWith, page):
    endpoint = "characters"
    params = {'nameStartsWith': nameStartsWith}
    characters, total_results = get_data(endpoint, params)
    return characters, total_results


def get_comics_list(titleStartsWith, page):
    endpoint = "comics"
    params = {'titleStartsWith': titleStartsWith}
    comics, total_results = get_data(endpoint, params)
    return comics, total_results


def get_creators_list(nameStartsWith):
    endpoint = "creators"
    params = {'nameStartsWith': nameStartsWith}
    return get_data(endpoint, params)


def get_events_list(nameStartsWith):
    endpoint = "events"
    params = {'nameStartsWith': nameStartsWith}
    return get_data(endpoint, params)


def get_series_list(titleStartsWith):
    endpoint = "series"
    params = {'titleStartsWith': titleStartsWith}
    return get_data(endpoint, params)


def get_story_by_id(story_id):
    endpoint = "stories/" + story_id
    return get_data(endpoint, {})


def get_serie_by_id(serie_id):
    endpoint = "series/" + serie_id
    return get_data(endpoint, {})


def get_event_by_id(event_id):
    endpoint = "events/" + event_id
    return get_data(endpoint, {})


def get_creator_by_id(creator_id):
    endpoint = "creators/" + creator_id
    return get_data(endpoint, {})


def get_character_by_id(character_id):
    endpoint = "characters/" + character_id
    return get_data(endpoint, {})


def get_comic_by_id(comic_id):
    endpoint = "comics/" + comic_id
    return get_data(endpoint, {})


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


# GET HASH OF URL
def getHash(ts):

    # CLAVES Y HASH NECESARIOS PARA LA PETICION
    publicKey = 'dbc203265f84033afd469a493cec6b27'
    privateKey = '1bd9e9686369a65ff11aa1e51919e884ad04765f'
    preHash = str(ts) + privateKey + publicKey
    # SE USA .encode PORQUE preHash ES UN STRING
    hash = hashlib.md5(preHash.encode()).hexdigest()
    return hash
