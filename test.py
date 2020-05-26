from main import Main

import matplotlib.pyplot as plt
import numpy as np


chanel = 0
sampleBeginning = 1.5
sampleEnd = 4
#piano frequency range
frequencyBeginning = 27.5
frequencyEnd= 4186
distance = 5
number = 6  #number of the notes to detect
threshhold = 1/3
fStartingNote = 440


m = Main(r"ressources\Recording.wav") #ressources\B flat Trupet.wav #ressources\Piano A.wav
m.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, threshhold , fStartingNote)

plt.plot(m.xvalues, m.values)

plt.show()

plt.plot(*m.fvalues_xy)
plt.plot(*m.extrema, "b.")
plt.plot(*m.mainFrequencies, "o")
#plt.xscale("log")
plt.show()

notes = m.notes
print(notes)
notes = m.removeRepetitions(notes)
notes = m.noteNames(notes)
print(notes)