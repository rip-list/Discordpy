import json
# import webbrowser
import spotipy

settings = {
<<<<<<< HEAD
    'token': '',
=======
    'token': '',
>>>>>>> 6243af2 (дописал ещё говнокода)
    'prefix': '-',
    'bot': 'ADOOM',
    'id': 1087784226272841749
}

spotify_info = {
    'USERNAME': 'rip-list',
<<<<<<< HEAD
    'CLIENT_ID': '67df0c7657a042b89a512693e1a288',
    'CLIENT_SECRET': '',
=======
    'CLIENT_ID': '67df0c7657a042b89a51269369e1a288',
    'CLIENT_SECRET': '',
>>>>>>> 6243af2 (дописал ещё говнокода)
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


<<<<<<< HEAD
class ParsJson:

    with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
=======
def ParsJson():
    with open('data.txt', 'w') as outfile:
        json.dumps(user)

    return True
>>>>>>> 6243af2 (дописал ещё говнокода)
