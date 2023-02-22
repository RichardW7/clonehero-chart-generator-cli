import requests
import constants
from gettoken import authenticate
from track import Track
from createchartfolder import folder

def main():
    token = authenticate(constants.CLIENT_ID, constants.CLIENT_SECRET)

    track_info = requests.get(constants.BASE_URL + "playlists/" + constants.PLAYLIST_ID, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }).json()

    tracks = {}

    for track in track_info["tracks"]["items"]:
        #make analysis call
        track_analysis = requests.get(constants.BASE_URL + "audio-analysis/" + track["track"]["id"], headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
        }).json()
        #declare object
        tracks[track["track"]["name"]] = Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"],
        track["track"]["album"]["name"], track["track"]["album"]["release_date"], track["track"]["duration_ms"], 
        track["track"]["album"]["images"][0], track_analysis["track"]["tempo"], track_analysis["beats"],
        track_analysis["bars"], track_analysis["tatums"], track_analysis["sections"], track_analysis["segments"], track_analysis["track"]["time_signature"])

    for i in tracks:
        folder(tracks[i])

if __name__ == "__main__":
    main()
