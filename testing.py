from main import Extractor, Transformator, Translator

import matplotlib.pyplot as plt
import numpy as np

from scipy.io import wavfile

transform = Transformator(r"ressources\B flat Trupet.wav") #ressources\Piano A.wav

plt.plot(*transform.transform(sample_beginning=1, sample_end=2, frequency_beginning = 0, frequency_end =  500, slicing=1, chunks = 10))
plt.plot(*transform.findextrema(), 'x')
plt.show()

# plt.plot(*transform.transform(sample_beginning=1, sample_end=1, frequency_beginning = 0, frequency_end =  4000, slicing=1, chunks = 10))
# plt.plot(*transform.findextrema(), 'x')

translator = Translator(r"ressources\B flat Trupet.wav") #ressources\60 Hz Test Tone-GqwFimG3X3w.wav

#transform.plot()
#TODO fix me!
plt.plot(translator.extract())
plt.show()
plt.plot(*translator.transform(sample_beginning=1, sample_end=2, frequency_beginning = 0, frequency_end =  500, slicing=1, chunks = 10))
#plt.plot(*translator.findextrema(), 'x')
plt.plot(*translator.findMainFrequencies(5), 'x')
plt.show()