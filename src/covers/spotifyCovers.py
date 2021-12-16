from urllib import parse
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def getAlbumCoverArt(albumName):
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Find album by name:
    results = sp.search(q = "album:" + albumName, type = "album")

    # Get the first album uri:
    album_id = results['albums']['items'][0]['uri']
    
    # Get album data:
    album_data = sp.album(album_id)
    
    # Get album image url:
    album_image_url = album_data["images"][0]["url"]
    
    return album_image_url