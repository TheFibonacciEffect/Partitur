import concurrent.futures
from main import Translator


translator = Translator(r"...")
sps = translator.samplesPerSecond
#this is the numpy array that has been split into segments, 1/16 note in length each, according to the samples per second
data = [[1,2,4,34,2], [123,415,2,65,46], [12,34,2134,15,345]]

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list(executor.map(   lambda x: translator.findMainFrequencies(5, data=x), data))

        #TODO what I want [[0], [0,4,7]] # a, a dur (a, c#, e), das ist 0, 4, 4+3 halbtonschritte, also kleine Terz und Quinte