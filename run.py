#TODO this whole file is hacky and should be reprogrammed. Shape the methods in main accordingly and don't write the run.py according to main, but rather the other way arround

import concurrent.futures
from main import Translator
import numpy as np
import os
from coloredOutput import style

translator = Translator(r"ressources\Piano A.wav")
#TODO read and split music
x = np.linspace(0.0, 1)
music = translator.extract(sampleEnd = -1)
sps = translator.samplesPerSecond

seconds = 1 #split every 10th second

splitLenghth = len(music)//sps  #one second in lenght, currently (I believe)
#this is the numpy array that has been split into segments, 1/10th seconds in length each, according to the samples per second
music =np.array_split(music, splitLenghth)


def noteMaker(data):
    print(style.BLUE +f"working on {os.getpid()}" + style.RESET)
    print(f"recieved data length: {len(data)}")
    mainFrequencies = translator.findMainFrequencies(5, data=x)[0]  #change number of notes here (currently 5)
    print(f"main frequencies {mainFrequencies}")
    return [  translator.frequencyToNoteValue(i) for i in range(len(mainFrequencies)) ] #this is a lost comprehension, to determine the NoteValue for each frequency in the list

#multiprossesing
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(1) as executor:
        #help(executor)
        notes = list(executor.map(noteMaker, music))
        print(notes)
        #TODO what I want [[0], [0,4,7]] # a, a dur (a, c#, e), das ist 0, 4, 4+3 halbtonschritte, also kleine Terz und Quinte