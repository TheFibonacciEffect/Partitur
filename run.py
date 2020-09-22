# pylint: skip-file
from main import Main
import concurrent.futures 


file = input("file: ")
sampleBeginning = input("beginning of Sample in seconds: ")
sampleEnd =       float(input("end of Sample in seconds: "))
threshhold =      float(input("threshhold to suppress noise: "))
numberOfNotes =   int(input("maximum number uf notes to detect: "))
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        m = Main(file)

        splitLengthinSeconds = 0.2
        # multithreading
        song = m.split(splitLengthinSeconds, sampleBeginning = sampleBeginning, sampleEnd = sampleEnd)

        notes = list(executor.map(lambda data: m.thread(data, threshhold, numberOfNotes), song))

        # every list in the list is a triad or more notes played at the same time [[0,12]] for example is an " a' " and an " a'' "
        notes = m.removeRepetitions(notes, removePartialRepetitions=True)
        notes = m.noteNames(notes)
        print(len(notes))
        print(notes)
        