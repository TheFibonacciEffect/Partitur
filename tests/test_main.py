# # an untested code is broken as designed

import sys
import pathlib
path = str(pathlib.Path(__file__).parent.parent)
sys.path.append(path)

from main import Main

import numpy as np
import pytest

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