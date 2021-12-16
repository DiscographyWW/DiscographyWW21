import os
from .trelloBoard import *
from .discographyReader import *
from covers.spotifyCovers import getAlbumCoverArt

def albumNameIsValid(albumName):
   if(len(albumName) > 5 and albumName[:4].isdigit() and albumName[4] == " "):
      return True
   else:
      return False
   
def createTrelloDiscographyBoard():
   result = ""
   errors = ""
   try:
      trello_board_url = createNewDiscographyBoard()
      result = f'Your board is aviable <a href="{trello_board_url}">here</a>.\n{result}'
   except Exception as e:
      print(f'ERROR:\n{e}') # For debugging purposes.
      return f'ERROR: {e}'
   
   try:
      trello_board_id = trello_board_url.split("/")[-1].strip()
      sorted_albums = sortAlbumsFromFile(os.getenv("DEFAULT_DISCOGRAPHY_FILE_NAME"))
      years = getYearsFomAlbums(sorted_albums)
      decades = GetDecadesFromYears(years)
      
      for decade in decades:
         decade_list_id = createTrelloList(trello_board_id, decade)
         fetched_albums = fetchAlbumsWithDecade(sorted_albums, decade)
         for album in fetched_albums:
            if(albumNameIsValid(album)):
               try:
                  albumCoverArt = getAlbumCoverArt(album[5:])
               except Exception as e:
                  print(f'ERROR: \n{e}') # For debugging purposes.
                  albumCoverArt = os.getenv("DEFAULT_ALBUM_COVER")
               createTrelloCard(decade_list_id, album, albumCoverArt)
            else:
               errors = f'{errors}<br>Invalid album name:"{album}"'
   except Exception as e:
               print(f'ERROR: \n{e}') # For debugging purposes.
               errors = f'{errors}<br>'
   if(errors != ""):
      errors = f'Problems found during the process:<br>{errors}'
   return f'{result}<br>{errors}'