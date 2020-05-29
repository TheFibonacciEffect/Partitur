# pylint: skip-file
from main import Main
import concurrent.futures 


threshhold = 1/5        #change the threshhold
numberOfNotes = 6     #change here to change the number of recorded notes

file = r"ressources\thegodfather.wav"   #input("file: ")
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        m = Main(file)

        splitLengthinSeconds = 0.2
        # multithreading
        song = m.split(splitLengthinSeconds, sampleBeginning = 0, sampleEnd = 5)

        notes = list(executor.map(lambda data: m.thread(data, threshhold, numberOfNotes), song))

        # every list in the list is a triad or more notes played at the same time [[0,12]] for example is an " a' " and an " a'' "
        notes = m.removeRepetitions(notes, removePartialRepetitions=True)
        notes = m.noteNames(notes)
        print(len(notes))
        print(notes)
        