# an untested code is broken as designed

# add parent dir, so tests can be imported
import sys
import pathlib
path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)

import numpy as np
import pytest

#import units to test
from main import Main

class TestMain():
    def test_main(self):
        chanel = 0
        sampleBeginning = 2
        sampleEnd = 3
        #piano frequency range
        frequencyBeginning = 27.5
        frequencyEnd= 4186
        distance = 5
        number = 6  #number of the notes to detect
        threshhold = 0.37999999999999945
        fStartingNote = 440
        main = Main(r"ressources\60 Hz Test Tone-GqwFimG3X3w.wav")
        main.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, threshhold, fStartingNote)
        noteValue = main.notes
        assert noteValue == [[-34]]

    def test_notwav(self):
        chanel = 0
        sampleBeginning = 2
        sampleEnd = 3
        #piano frequency range
        frequencyBeginning = 27.5
        frequencyEnd= 4186
        distance = 5
        number = 6  #number of the notes to detect
        threshhold = 0.37999999999999945
        fStartingNote = 440

        main = Main(r"C:\Users\caspa\Documents\Code\Python Projects\Partitur\ressources\Recording (8).m4a")
        main.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, threshhold, fStartingNote)
        noteValue = main.notes
        #main.removeRepetitions(noteValue)
        names = main.note_names
        assert noteValue == [[7,0,3]] and names == [["a","c","e"]] #noteValue == [[7, 12, 15]] and names == [["e", "a","c"]]