from main import Extractor, Transformator

extract = Extractor(r"ressources\60 Hz Test Tone-GqwFimG3X3w.wav")

import matplotlib.pyplot as plt
import numpy as np

#extract.plot(sample_beginning= 4.2,sample_end=4.5)

transform = Transformator(r"ressources\60 Hz Test Tone-GqwFimG3X3w.wav")

#transform.plot()
plt.plot(*transform.transform())
plt.plot(*transform.findextrema(), 'x')
plt.show()
