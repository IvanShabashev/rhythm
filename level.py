# RTM file format:
# song name [null byte]
# artist name [null byte]
# hit times in milliseconds
# stored as 32-bit little-endian unsigned integers
# an RTM file should be named
# [filename of the song audio including extension].rtm
import struct
import os


class Level:
    def __init__(self, fileName):
        # save filename for later use
        self.fileName = fileName
        # find the data file in the levels folder and read it
        dataFile = open(os.path.join("levels", fileName), "rb").read()
        # save artist and song name for later use
        self.name = dataFile.split(b"\0")[0].decode()
        self.artist = dataFile.split(b"\0")[1].decode()
        # Find the second null byte (end of artist's name)
        n = 0
        for i in range(len(dataFile)):
            if dataFile[i] == 0:
                if n == 1:
                    break
                else:
                    n = 1
        # Store everything after the second null byte
        # this will be the hit data
        hitData = dataFile[i+1:]
        # get the song name from the filename
        # by removing the "rtm" extension
        self.songName = os.path.splitext(self.fileName)[0]
        self.songName = os.path.join("levels", self.songName)
        # read in the hit data
        self.hits = []
        for i in range(0, len(hitData), 4):
            self.hits.append(struct.unpack("<I", hitData[i:i+4])[0])
