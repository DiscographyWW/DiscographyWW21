import os
import re

def sortAlbumsFromFile(filename):
    try:
        albums = list()
        with open(filename, 'r') as fin:
            for line in fin:
                albums.append(line)
        albums.sort()
        fetchAlbumsWithDecade(albums, "80s")
        return albums
    except Exception as e:
        print(f'ERROR:\n{e}') # For debugging purposes.
        return False

def getYearsFomAlbums(alumbsList):
    try:
        years = list()
        for album in alumbsList:
            album_year = album[0:4]
            if album_year not in years:
                years.append(album_year)
        return(years)
    except Exception as e:
        print(f'ERROR:\n{e}') # For debugging purposes.
        return False

def GetDecadesFromYears(yearsList):
    try:
        decades = list()
        for year in yearsList:
            decade = year[2] + "0s"
            if(decade not in decades):
                decades.insert(0, decade)
        return decades
    except Exception as e:
        print(f'ERROR:\n{e}') # For debugging purposes.
        return False
    
def fetchAlbumsWithDecade(albumsList, decade):
    try:
        decadeAlbums = list()
        for album in albumsList:
            titleDecade = album[2] + "0s"
            if(titleDecade == decade and album not in decadeAlbums):
                decadeAlbums.append(album)
        return decadeAlbums
    except Exception as e:
        print(f'ERROR:\n{e}') # For debugging purposes.
        return False