from main import Extractor, Transformator, Translator

import matplotlib.pyplot as plt
import numpy as np

sampleBeginning = 10
sampleEnd = 12

translator = Translator(r"ressources\Piano A.wav")

mainFrequencies = translator.findMainFrequencies(2, sampleBeginning = sampleBeginning, sampleEnd = sampleEnd)

plt.plot(*translator.transform(sampleBeginning = sampleBeginning, sampleEnd = sampleEnd),"-")
plt.plot(*mainFrequencies,"x")

plt.show()

print(
    translator.frequencyToNoteValue(fStartingNote = 440,    #prints the note value difference between an "a" (440Hz) and the played note 
        frequency= mainFrequencies[0][0])) #first element of x-coorrdinate(frequencies)

#if there is more then one note played, you can itterate over them:

for i in range(len(mainFrequencies[0])):
    print(translator.frequencyToNoteValue(mainFrequencies[0][i]))