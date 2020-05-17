from main import Extractor, Transformator, Translator

import matplotlib.pyplot as plt
import numpy as np

translator = Translator(r"ressources\Piano A.wav")

plt.plot(*translator.transform(sampleBeginning = 10, sampleEnd = 12),"-")
plt.plot(*translator.findMainFrequencies(2, sampleBeginning = 10, sampleEnd = 12),"x")

plt.show()
plt.plot(*translator.findMainFrequencies(2, sampleBeginningg=1, sampleEnd=2, frequencyBeginning = 0, frequency_end =  500, slicing=1, chunks = 1), 'x')
plt.show()