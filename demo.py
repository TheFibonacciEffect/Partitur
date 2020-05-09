from main import Extractor, Transformator

extract = Extractor(r"ressources\thegodfather.wav")

import matplotlib.pyplot as plt
import numpy as np

extract.plot(sample_beginning= 1,sample_end=2)

transform = Transformator(r"ressources\thegodfather.wav") #ressources\Piano A.wav

#transform.plot()
plt.plot(*transform.transform(sample_beginning=1, sample_end=2, frequency_beginning = 0, frequency_end =  500, slicing=1, chunks = 10))
plt.plot(*transform.findextrema(), 'x')
plt.show()
