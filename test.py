from main import Main

import matplotlib.pyplot as plt
import numpy as np

file = r"\ressources\Recording (8).m4a" #input("file: ")
chanel = 0
sampleBeginning = 2
sampleEnd = 3
#piano frequency range
frequencyBeginning = 27.5
frequencyEnd= 4186
distance = 5
number = 6  #number of the notes to detect
threshhold = 0.37999999999999945
fStartingNote = 440


m = Main(file) #ressources\B flat Trupet.wav #ressources\Piano A.wav
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