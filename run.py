import concurrent.futures
from main import Translator

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list(executor.map(function, list))

        #TODO what I want [[0], [0,4,7]] # a, a dur (a, c#, e), das ist 0, 4, 4+3 halbtonschritte, also kleine Terz und Quinte