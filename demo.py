from main import Extractor, Transformator, Translator
import matplotlib.pyplot as plt
import numpy as np

extract = Extractor(r"ressources\Piano A.wav")



extract.plot(sampleBeginning= 1,sampleEnd=2)

transform = Transformator(r"ressources\Piano A.wav")

#transform.plot()
plt.plot(*transform.transform(sampleBeginning=1, sampleEnd=2, frequencyBeginning = 0, frequency_end =  500))
plt.plot(*transform.findextrema(), 'x')
plt.show()

translator = Translator(r"ressources\Piano A.wav") #ressources\60 Hz Test Tone-GqwFimG3X3w.wav

plt.show()
plt.plot(*translator.transform(sampleBeginning=1, sampleEnd=2, frequencyBeginning = 0, frequency_end =  500))
plt.plot(*translator.findMainFrequencies(5), 'x')
plt.show()