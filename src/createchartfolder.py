import os
import urllib.request
from createinifile import ini
from createchartfile import chart
from downloadsongs import getmp3
import constants

def folder(track):

    directory = track.artist + " - " + track.name

    if os.path.exists(constants.CLONE_HERO_PATH + directory):
        os.system("rm -r " + constants.CLONE_HERO_PATH_QUOTED + "\"" + directory + "\"")

    os.mkdir(constants.CLONE_HERO_PATH + directory)

    getmp3(track, directory)

    imgURL = track.img_url["url"]
    urllib.request.urlretrieve(imgURL, constants.CLONE_HERO_PATH + directory + "/album.png")
    os.system("ffmpeg -y -i " + constants.CLONE_HERO_PATH_QUOTED + "\"" + directory + "\"/\"" + directory + ".mp3\"  -strict -2 -acodec vorbis -ac 2 -aq 50 " + constants.CLONE_HERO_PATH_QUOTED + "\"" + directory + "\"/song.ogg")
    os.system("rm " + constants.CLONE_HERO_PATH_QUOTED + "\"" + directory + "\"/\"" + directory + ".mp3\"")

    sourceFile = open("song.ini", "w")
    ini(track, sourceFile)
    sourceFile.close()

    os.system("mv " + constants.GENERATOR_PATH + "song.ini " + constants.CLONE_HERO_PATH_QUOTED + "\"" + directory + "\"/song.ini")

    sourceFile = open("notes.chart", "w")
    chart(track, sourceFile)
    sourceFile.close()

    os.system("mv " + constants.GENERATOR_PATH + "notes.chart " + constants.CLONE_HERO_PATH_QUOTED + "\"" + directory + "\"/notes.chart")