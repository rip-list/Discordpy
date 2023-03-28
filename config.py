import json
# import webbrowser
import spotipy

settings = {
    'token': '',
    'prefix': '-',
    'bot': 'ADOOM',
    'id': 1087784226272841749
}

spotify_info = {
    'USERNAME': 'rip-list',
    'CLIENT_ID': '67df0c7657a042b89a512693e1a288',
    'CLIENT_SECRET': '',
    'redirectURL': "http://example.com"
}

info = {
    'creator': 'rip-list'
}

oauth_object = spotipy.SpotifyOAuth(spotify_info["CLIENT_ID"], spotify_info["CLIENT_SECRET"],
                                    spotify_info['redirectURL'])
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()


class ParsJson:

    with open('data.txt', 'w') as outfile:
        json.dumps(user, sort_keys=True, indent=4)
