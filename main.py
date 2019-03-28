import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

import config.client as c
import analysis as a

username = input("Insira nome de usuario Spotify -> ")
client_credentials_manager = SpotifyClientCredentials(client_id=c.client_id, client_secret=c.client_secret)
scope = 'user-library-read playlist-read-private'
try:
  token = util.prompt_for_user_token(username=username,
                                      scope=scope,
                                      client_id=c.client_id,
                                      client_secret=c.client_secret,
                                      redirect_uri=c.redirect_uri)
  sp = spotipy.Spotify(auth=token)
except:
  print('Token is not accessible for '+username)

escolha = 0
while(escolha != 4):
  

  print("Escolha o que fazer\n 1 - Ver todas playlists de "+username+"\n"+
        " 2 - Salvar conteudo de uma PL em JSON\n"+
        " 3 - Salvar audio features de uma PL em .csv\n 4 - Sair")
  escolha = int(input("   -> "))

  if(escolha == 1):
    a.get_user_playlist(username, sp)
  elif(escolha == 2):
    playlistID = input("Entre um PlaylistID -> ")
    a.get_playlist_content(username, playlistID, sp)
  elif(escolha == 3):
    playlistID = input("Entre um PlaylistID -> ")
    a.get_playlist_audio_features(username, playlistID, sp)





