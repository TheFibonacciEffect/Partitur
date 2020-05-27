from main import Main
import concurrent.futures 


file = input("file: ")
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        m = Main(file)

        splitLengthinSeconds = 0.2
        # multithreading
        song = m.split(splitLengthinSeconds, sampleBeginning = 30, sampleEnd = 40)

        notes = list(executor.map(m.thread, song))

        # every list in the list is a triad or more notes played at the same time [[0,12]] for example is an " a' " and an " a'' "
        notes = m.removeRepetitions(notes)
        notes = m.noteNames(notes)
        print(len(notes))
        print(notes)