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

threshhold = 0

for i in range(10):
    notes = m.main(chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, threshhold , fStartingNote)
    print(f"notes : {notes}")
    if notes == ["a", "c", "e"]:
        threshhold -= 1/2**i
    else:
        threshhold += 1/2**i
    
print(threshhold)