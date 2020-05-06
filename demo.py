from main import Extractor, Transformator

#extract = Extractor(r"ressources\Piano A.wav")

import matplotlib.pyplot as plt
import numpy as np

#extract.plot(sample_beginning= 0,sample_end=1)

transform = Transformator(r"ressources\B flat Trupet.wav") #ressources\Piano A.wav

#transform.plot()
plt.plot(*transform.transform(sample_beginning=1, sample_end=-1, frequency_beginning = 0, frequency_end =  4000, slicing=1, chunks = 1))
#plt.plot(*transform.findextrema(), 'x')
plt.show()
