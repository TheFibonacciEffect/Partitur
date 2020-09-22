from main import Main

import matplotlib.pyplot as plt
import numpy as np

file = input("file: ") #\ressources\Recording (8).m4a
sampleBeginning = float(input("beginning of Sample in seconds: "))
sampleEnd =       float(input("end of Sample in seconds: "))
threshhold =      float(input("threshhold to suppress noise: "))
number =          int(input("maximum number of notes to detect: "))

chanel = 0
#piano frequency range
frequencyBeginning = 27.5
frequencyEnd= 4186
distance = 5
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