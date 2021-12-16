import os
import requests
import json
from datetime import datetime

def createTrelloCard(trelloListId, trelloCardName, trelloCardImage):
   try:
      url = f'{os.getenv("TRELLO_API_URL")}/cards'
      headers = {"Accept": "application/json"}
      query = {"name": trelloCardName, "desc": trelloCardName, "pos": "bottom", "idList": trelloListId, "key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")}
      if(trelloCardImage):
         query = {"name": trelloCardName, "desc": trelloCardName, "pos": "bottom", "urlSource":trelloCardImage, "idList": trelloListId, "key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")}
      response = requests.request("POST", url, headers=headers, params=query)
      print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) # For debugging purposes.
      return True
   except Exception as e:
      print(f'ERROR: \n{e}') # For debugging purposes.
      return False

def createTrelloList (trelloBoardId, trelloListName):
   try:
      url = f'{os.getenv("TRELLO_BOARD_URL")}{trelloBoardId}/lists'
      headers = {"Accept": "application/json"}
      query = {"name": trelloListName, "key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")}
      response = requests.request("POST", url, headers=headers, params=query)
      print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) # For debugging purposes.
      return response.json()["id"]
   except Exception as e:
      print(f'ERROR:\n{e}') # For debugging purposes.
      return False
   
def createTrelloBoard(trelloBoardName):
   try:
      url = os.getenv("TRELLO_BOARD_URL")
      querystring = {"name": trelloBoardName,  "defaultLists": "false", "key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")}
      response = requests.request("POST", url, params=querystring)
      board_id = response.json()["shortUrl"].split("/")[-1].strip()
      if board_id:
         return response.json()["shortUrl"]
      else:
         response_message = response.json()["message"]
         return f'ERROR: {response_message}'
   except Exception as e:
      print(f'ERROR:\n{e}') # For debugging purposes.
      return f'ERROR: {e}'

def createNewDiscographyBoard():
   return createTrelloBoard(f'{os.getenv("TRELLO_BOARD_DEFAULT_NAME")} {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')