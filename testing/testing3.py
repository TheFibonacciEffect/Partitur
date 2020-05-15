from main import Extractor, Transformator

extract = Extractor(r"ressources\thegodfather.wav")

import matplotlib.pyplot as plt
import numpy as np

extract.plot(sample_beginning= 1,sample_end=5)

transform = Transformator(r"ressources\60 Hz Test Tone-GqwFimG3X3w.wav") #ressources\Piano A.wav #r"ressources\thegodfather.wav"

#transform.plot()
plt.plot(*transform.transform(sample_beginning=1, sample_end=10, frequency_beginning = 55, frequency_end =  65, slicing=1, chunks = 100))
plt.plot(*transform.findextrema(), 'x')
plt.show()
