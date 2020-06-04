from main import Main

file = r"C:\Users\caspa\Documents\Sound recordings\Recording (8).m4a"

m = Main(file)

chanel = 0
sampleBeginning = 2
sampleEnd = 3
#piano frequency range
frequencyBeginning = 27.5
frequencyEnd= 4186
distance = 5
number = 6  #number of the notes to detect
fStartingNote = 440

threshhold = 1

notes = []

while notes != [["a", "c", "e"]] and threshhold > 0:
    notes = m.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, threshhold , fStartingNote)
    threshhold -= 0.02

print(threshhold)