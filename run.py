from main import Main
import concurrent.futures 

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        m = Main(r"ressources\Recording.wav") #ressources\Piano A.wav

        splitLengthinSeconds = 0.5
        # multiprocessing
        song = m.split(splitLengthinSeconds, sampleBeginning = 0, sampleEnd = -1)

        notes = list(executor.map(m.thread, song))

        # every list in the list is a triad or more notes played at the same time [[0,12]] for example is an " a' " and an " a'' "
        print(notes)