from main import Main

import matplotlib.pyplot as plt
import numpy as np

sampleBeginning = 10
sampleEnd = 12

chanel = 0
sampleBeginning = 0
sampleEnd = 2
#piano frequency range
frequencyBeginning = 27.5
frequencyEnd= 4186
distance = 5
number = 3  #number of the notes to detect
fStartingNote = 440

m = Main(r"ressources\Piano A.wav") #ressources\B flat Trupet.wav
m.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, fStartingNote)

plt.plot(m.xvalues, m.values)

plt.show()

plt.plot(*m.fvalues_xy)
plt.plot(*m.extrema, "b.")
plt.plot(*m.mainFrequencies, "o")
#plt.xscale("log")
plt.show()