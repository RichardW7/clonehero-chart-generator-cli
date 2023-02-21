import os
import requests
from gettoken import authenticate
from track import Track
# from downloadsongs import getmp3s
from createchartfile import chart
from createchartfolder import folder
import math
import bisect

def get_frets(beats, sections, segments, tatums):
    frets = []
    for i in beats:
        frets.append((beats[i].start, 4))
    # for i in sections:
    #     frets.append((sections[i].start, 3))
    # for i in segments:
    #     frets.append((segments[i].start, ))
    for i in tatums:
        frets.append((tatums[i].start, 3))

def main():

    CLIENT_ID = 'fb4104f5ed544c8c8cb7a77cca56be0f'
    CLIENT_SECRET = '56bcda3bbca9479aa61acfadd75b7556'
    BASE_URL = 'https://api.spotify.com/v1/'
    USER_ID = 'richard7w'
    PLAYLIST_ID = '7BXlR474AbcPBTYDtkCLtF?si=d9bbf0793a554da6&pt=de35208ae88623f5a7f0e89338b3bcf7'

    token = authenticate(CLIENT_ID, CLIENT_SECRET)

    track_info = requests.get(BASE_URL + "playlists/" + PLAYLIST_ID, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }).json()

    tracks = {}

    for track in track_info["tracks"]["items"]:
        #make analysis call
        track_analysis = requests.get(BASE_URL + "audio-analysis/" + track["track"]["id"], headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
        }).json()
        #declare object
        sourceFile = open("track.txt", "w")
        tracks[track["track"]["name"]] = Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"],
        track["track"]["album"]["name"], track["track"]["album"]["release_date"], track["track"]["duration_ms"], 
        track["track"]["album"]["images"][0], track_analysis["track"]["tempo"], track_analysis["beats"],
        track_analysis["bars"], track_analysis["tatums"], track_analysis["sections"], track_analysis["segments"], track_analysis["track"]["time_signature"])
        sourceFile = open("track.txt", "w")
        print(tracks[track["track"]["name"]].frets, file=sourceFile)

    for i in tracks:
        folder(tracks[i])


    

if __name__ == "__main__":
    main()
