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


# GET CHARACTERS LIST
def get_characters_list(nameStartsWith):
    BASE_URL = "https://gateway.marvel.com/v1/public/characters"
    hash = getHash(1000)
    args = {
        'nameStartsWith': nameStartsWith,
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 20,
        'offset': 0
    }
    return get_data_list(BASE_URL, args)


# GET COMICS LIST
def get_comics_list(titleStartsWith):
    BASE_URL = "https://gateway.marvel.com/v1/public/comics"
    hash = getHash(1000)
    args = {
        'titleStartsWith': titleStartsWith,
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 20,
        'offset': 0
    }
    return get_data_list(BASE_URL, args)


# GET CREATORS LIST
def get_creators_list(nameStartsWith):
    BASE_URL = "https://gateway.marvel.com/v1/public/creators"
    hash = getHash(1000)
    args = {
        'nameStartsWith': nameStartsWith,
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 20,
        'offset': 0
    }
    return get_data_list(BASE_URL, args)


# GET EVENTS LIST
def get_events_list(nameStartsWith):
    BASE_URL = "https://gateway.marvel.com/v1/public/events"
    hash = getHash(1000)
    args = {
        'nameStartsWith': nameStartsWith,
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 20,
        'offset': 0
    }
    return get_data_list(BASE_URL, args)


# GET SERIES LIST
def get_series_list(titleStartsWith):
    BASE_URL = "https://gateway.marvel.com/v1/public/series"
    hash = getHash(1000)
    args = {
        'titleStartsWith': titleStartsWith,
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
        'limit': 20,
        'offset': 0
    }
    return get_data_list(BASE_URL, args)


# GET STORY BY ID
def get_story_by_id(story_id):
    BASE_URL = "https://gateway.marvel.com/v1/public/stories/" + story_id
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
    }
    return get_data_list(BASE_URL, args)


# GET SERIE BY ID
def get_serie_by_id(serie_id):
    BASE_URL = "https://gateway.marvel.com/v1/public/series/" + serie_id
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
    }
    return get_data_list(BASE_URL, args)


# GET EVENT BY ID
def get_event_by_id(event_id):
    BASE_URL = "https://gateway.marvel.com/v1/public/events/" + event_id
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
    }
    return get_data_list(BASE_URL, args)


# GET CREATOR BY ID
def get_creator_by_id(creator_id):
    BASE_URL = "https://gateway.marvel.com/v1/public/creators/" + creator_id
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
    }
    return get_data_list(BASE_URL, args)


# GET CHARACTER BY ID
def get_character_by_id(character_id):
    BASE_URL = "https://gateway.marvel.com/v1/public/characters/" + character_id
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
    }
    return get_data_list(BASE_URL, args)


# GET ONE COMIC BY ID
def get_comic_by_id(comic_id):
    BASE_URL = "https://gateway.marvel.com/v1/public/comics/" + comic_id
    hash = getHash(1000)
    args = {
        'ts': 1000,
        'apikey': 'dbc203265f84033afd469a493cec6b27',
        'hash': hash,
    }
    return get_data_list(BASE_URL, args)


# GET RESULTS OF JSON
def getJsonList(responseJson):
    json_List = []
    for json_element in responseJson['data']['results']:
        json_List.append(json_element)
    return json_List


# GET DATA LIST RESPONSE
def get_data_list(url, args):
    data_list = []
    response = requests.get(url, params=args)
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        data_list = getJsonList(responseJson)

    return data_list


# GET HASH OF URL
def getHash(ts):

    # CLAVES Y HASH NECESARIOS PARA LA PETICION
    publicKey = 'dbc203265f84033afd469a493cec6b27'
    privateKey = '1bd9e9686369a65ff11aa1e51919e884ad04765f'
    preHash = str(ts) + privateKey + publicKey
    # SE USA .encode PORQUE preHash ES UN STRING
    hash = hashlib.md5(preHash.encode()).hexdigest()
    return hash
