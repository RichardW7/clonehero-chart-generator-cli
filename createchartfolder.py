import os
import urllib.request
from createinifile import ini
from createchartfile import chart
from downloadsongs import getmp3

def folder(track):

    directory = track.artist + " - " + track.name

    if os.path.exists("/Users/richardwills/Clone Hero/Songs/Generated/" + directory):
        os.system("rm -r /Users/richardwills/\"Clone Hero\"/Songs/Generated/\"" + directory + "\"")

    os.mkdir("/Users/richardwills/Clone Hero/Songs/Generated/" + directory)

    getmp3(track, directory)

    imgURL = track.img_url["url"]
    urllib.request.urlretrieve(imgURL, "/Users/richardwills/Clone Hero/Songs/Generated/" + directory + "/album.png")
    os.system("ffmpeg -y -i /Users/richardwills/\"Clone Hero\"/Songs/Generated/\"" + directory + "\"/\"" + directory + ".mp3\"  -strict -2 -acodec vorbis -ac 2 -aq 50 /Users/richardwills/\"Clone Hero\"/Songs/Generated/\"" + directory + "\"/song.ogg")
    os.system("rm /Users/richardwills/\"Clone Hero\"/Songs/Generated/\"" + directory + "\"/\"" + directory + ".mp3\"")

    sourceFile = open("song.ini", "w")
    ini(track, sourceFile)
    sourceFile.close()

    os.system("mv /Users/richardwills/Development/clonehero-song-maker/song.ini /Users/richardwills/\"Clone Hero\"/Songs/Generated/\"" + directory + "\"/song.ini")

    sourceFile = open("notes.chart", "w")
    chart(track, sourceFile)
    sourceFile.close()

    os.system("mv /Users/richardwills/Development/clonehero-song-maker/notes.chart /Users/richardwills/\"Clone Hero\"/Songs/Generated/\"" + directory + "\"/notes.chart")