from main import Extractor, Transformator, Translator

import matplotlib.pyplot as plt
import numpy as np

transform = Transformator(r"ressources\60 Hz Test Tone-GqwFimG3X3w.wav") #ressources\Piano A.wav

#transform.plot()
# plt.plot(*transform.transform(sample_beginning=1, sample_end=1, frequency_beginning = 0, frequency_end =  4000, slicing=1, chunks = 10))
# plt.plot(*transform.findextrema(), 'x')

translator = Translator(r"ressources\60 Hz Test Tone-GqwFimG3X3w.wav")
x =  translator.findMainFrequencies(5)
print(x)
# plt.show()