import requests


def find_album_details(album):

    endpoint = f"http://ws.audioscrobbler.com//2.0/?method=album.search&album={album}&api_key=979f71b2b3e515ab22b3993175b669e1&format=json"
    text = requests.get(endpoint)
    text2 = text.json()['results']['albummatches']
    album_name = text2['album'][0]['name']
    artist = text2['album'][0]['artist']
    album_link = text2['album'][0]['url']
    image = text2['album'][0]['image'][3]['#text']

    dictionary_entry = {
        "album_name": album_name,
        "artist": artist,
        "link": album_link,
        "image": image
    }
    return dictionary_entry


def find_multiple_albums(album_list):
    api_list = []
    for alb in album_list:
        endpoint = f"http://ws.audioscrobbler.com//2.0/?method=album.search&album={alb}&api_key=979f71b2b3e515ab22b3993175b669e1&format=json"
        text = requests.get(endpoint)
        text2 = text.json()['results']['albummatches']
        album_name = text2['album'][0]['name']
        artist = text2['album'][0]['artist']
        album_link = text2['album'][0]['url']
        image = text2['album'][0]['image'][3]['#text']

        dictionary_entry = {
            "album_name": album_name,
            "artist": artist,
            "link": album_link,
            "image": image
        }
        api_list.append(dictionary_entry)
        return api_list


