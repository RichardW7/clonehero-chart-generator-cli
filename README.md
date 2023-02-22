# clonehero-chart-generator
## Setup
1. Create a spotify developer dashboard https://developer.spotify.com/dashboard/login (this gives us access to spotify API)
2. Add these to the constants.py file:
  - client id (CLIENT_ID)
  - client secret (CLIENT_SECRET)
  - redirect uri (REDIRECT_URI)
  - user id (USER_ID)
  - playlist id of the playlist you want to use (PLAYLIST_ID)
3. Setup paths (easiest method is to navigate to the directory you want and use: `pwd`)
  - add a path for where you want the songs to be ex. `/this/is an/example/path` (CLONE_HERO_PATH)
  - if the previous path has any spaces add quotes (the character for this is `\"`) ex. `/this/\"is an\"/example/path` (CLONE_HERO_PATH_QUOTED)
  - add the path of this repository (GENERATOR_PATH)
5. Run `pip install requirements.txt`
6. Install ffmpeg `brew install ffmpeg`
7. Run the script `python getplaylist.py`
