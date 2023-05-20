import hashlib
import requests
import json


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
