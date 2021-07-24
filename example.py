import requests
import json

anime_list = [
    ('hunter x hunter', 5)
]

def feeling_lucky(q):
    API_KEY = 'AIzaSyApbt_4fbeFCed0Wuu9qZ6ZTu7XJmnn4bQ'
    params = {
        'q': q,
        'key': API_KEY,
    }
    endpoint = 'https://www.googleapis.com/youtube/v3/search'
    response = requests.get(endpoint, params=params)
    video_id = response.json()['items'][0]['id']['videoId']
    return f'https://www.youtube.com/watch?v={video_id}'

for anime, count in anime_list:
    for i in range(count):
        print(feeling_lucky(f'{anime} op {i}'))
        print(feeling_lucky(f'{anime} ed {i}'))