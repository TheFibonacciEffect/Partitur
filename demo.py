from main import Extractor, Transformator

extract = Extractor(r"60 Hz Test Tone-GqwFimG3X3w.wav")

import matplotlib.pyplot as plt
import numpy as np

#extract.plot(sample_beginning= 4.2,sample_end=4.5)

Transformator(r"60 Hz Test Tone-GqwFimG3X3w.wav").plot(0)