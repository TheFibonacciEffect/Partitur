from main import Extractor, Transformator

extract = Extractor(r"ressources\thegodfather.wav")

import matplotlib.pyplot as plt
import numpy as np

extract.plot(sample_beginning= 0,sample_end=1)

transform = Transformator(r"ressources\thegodfather.wav")

#transform.plot()
plt.plot(*transform.transform(sample_beginning=0, sample_end=1, frequency_beginning = 0, frequency_end =  4000, slicing=1))
plt.plot(*transform.findextrema(), 'x')
plt.show()
