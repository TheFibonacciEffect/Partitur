from main import Main

import matplotlib.pyplot as plt
import numpy as np

sampleBeginning = 10
sampleEnd = 12

chanel = 0
sampleBeginning = 0
sampleEnd = 2
frequencyBeginning = 0
frequencyEnd=1000
distance = 5
number = 2  #number of the notes to detect
fStartingNote = 440

m = Main(r"ressources\Piano A.wav")
m.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, fStartingNote)

plt.plot(m.xvalues, m.values)

plt.show()

plt.plot(*m.fvalues_xy)
plt.plot(*m.extrema, "b.")
plt.plot(*m.mainFrequencies, "o")
plt.show()