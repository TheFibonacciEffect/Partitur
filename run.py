from main import Main
import concurrent.futures 


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(1) as executor:
        m = Main(r"ressources\Piano A.wav")

        splitLengthinSeconds = 3
        song = m.split(splitLengthinSeconds, sampleBeginning = 0, sampleEnd = -1)

        notes = list(executor.map(m.thread, song))

        #every list in the list is a triad [[0,12]] for example is an " a' " and an " a'' "
        print(notes)