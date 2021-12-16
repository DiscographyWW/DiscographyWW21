from flask import Flask
from flask_cors import CORS
from boards.discographyBoard import createTrelloDiscographyBoard
# from covers.spotifyCovers import getAlbumCoverArt

app = Flask(__name__)

# Here we define what happens when the specified route is requested:
@app.route("/")
def index():
    # return getAlbumCoverArt("The Times They Are a-Changin")
    return createTrelloDiscographyBoard()

if __name__ == "__main__":
    """
    Set DEBUG to TRUE for testing the code. It will reset the server 
    automatically if any changes are mede into the code. Please
    set DEBUG to  FALSE in a production environment.
    """
    app.run(debug=True)