from main import Extractor, Transformator, Translator
import matplotlib.pyplot as plt
import numpy as np

extract = Extractor(r"ressources\Piano A.wav")



extract.plot(sample_beginning= 1,sample_end=2)

transform = Transformator(r"ressources\Piano A.wav") #ressources\Piano A.wav

#transform.plot()
plt.plot(*transform.transform(sample_beginning=1, sample_end=2, frequency_beginning = 0, frequency_end =  500, slicing=1, chunks = 10))
plt.plot(*transform.findextrema(), 'x')
plt.show()

translator = Translator(r"ressources\Piano A.wav") #ressources\60 Hz Test Tone-GqwFimG3X3w.wav

plt.show()
plt.plot(*translator.transform(sample_beginning=1, sample_end=2, frequency_beginning = 0, frequency_end =  500, slicing=1, chunks = 10))
plt.plot(*translator.findMainFrequencies(5), 'x')
plt.show()