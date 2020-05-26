from scipy.fft import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from os.path import isfile
from coloredOutput import style
import os

class Extractor:
    """class used to extract a numpy array from a .wav file
    
    input:
        path to .wav
    
    methods:
        extract, returns the data as a np array
        plot(), plots it uning the matplotlib    
    """
    def __init__(self, file):
        if isfile(file):
            pass    
        else:
            file = file.replace("\\", "/" )    #UNIX uses foreward slashes instead of backslashes

        #if it is not a wavfile, transform it using ffmpeg (not yet tested, TODO)
        if file[-4:] != ".wav":
            os.system(f"ffmpeg -i {file} {file[:-4]}.wav")
            self.file = {file[:-4]} +".wav"
        else:
            self.file = file
            
    def extract(self, channel = 0, sampleBeginning =0, sampleEnd = -1): #TODO extract x and y coordinates, not just y (need to change in other methods as well)
        """input: channel (mostly 1 or 0), sampleBeginning (seconds), sampleEnd (seconds)
        output: the data of the channel using a numphy array """
        fs, data = wavfile.read(self.file) #extract data
        self.data = data
        self.samplesPerSecond = fs
        self.lenght = len(data)
        sampleBeginning, sampleEnd = int(sampleBeginning * self.samplesPerSecond), int(sampleEnd * self.samplesPerSecond)
        self.data = self.data[:,channel][sampleBeginning:sampleEnd]

        #throw exeption, when data is empty (all zeros)
        if all(flag == 0 for flag in self.data):
            raise LookupError(f"""the data is empty, the wavefile could not be read, maybe there is no music at that time?
            Try to readjust the timeframe and try again.
        here is the data: {self.data}""")

        #when data is empty, raise exeption
        if sampleBeginning == sampleEnd:
            raise IndexError("starting and ending point are the same")

        return self.data


    def plot(self, channel = 0,sampleEnd = None, sampleBeginning = 0): #in seconds
        """ input: channel (std = 0), sampleEnd in seconds, sampleBeginning in seconds
        plots the music using matplotlib, the self.extract() method will have to be called first """
        self.extract()


        if sampleEnd == None:
            sampleEnd = self.extract(channel = 0).__len__() // self.samplesPerSecond
        
        x = np.arange(sampleBeginning, sampleEnd, 1/self.samplesPerSecond) #start, stop, step

        #transform
        sampleBeginning = int(sampleBeginning * self.samplesPerSecond)
        sampleEnd = int(sampleEnd * self.samplesPerSecond) 
        sample_length = sampleEnd - sampleBeginning

        y = self.data[sampleBeginning :sampleEnd]
        plt.plot(x,y)
        plt.show()




class Transformator():
    """Fourrier transforms given data
    inherits from Extractor
    methods:
        transform
        find extrema
        plot
    fields:
        fdata:  contains x and y coordinates of transformed data
    """

    def __init__(self):
        pass

    def transform(self, y, frequencyBeginning = 300, frequencyEnd =  1000, **kwargs):
        """the fourrier transform gives a representation of the frequencies in the input array
        fourrier transforms given array, returns (xf,yf)
        slicing improves processing spead and memory usage
        returns:
            xf: x coordinate linspace
            yf: fourrier transform of input array"""

        N = y.__len__()

        #TODO the chunking scales down the transform. This dosn't work.
        #chunk data & generate np.array

        #Come back and increment this number after you attempt to optimize this resource-heavy function and fail: 3
        yf = fft(y, overwrite_x=True, workers=1)

        T = 1.0 / self.samplesPerSecond
        frequencyBeginningIndex = int(frequencyBeginning*T*N)
        frequencyEndIndex = int(frequencyEnd*T*N)
        yf = yf[frequencyBeginningIndex:frequencyEndIndex]
        N = yf.__len__()
        xf = np.linspace(frequencyBeginning, frequencyEnd, N)
        return xf, np.abs(yf)
        


    # def fplot(self,channel=0,sampleBeginning=0,sampleEnd=-1, frequencyBeginning = 55, frequency_end =  65): #Low C = 130 Hz middle c = 261 Hz, a' = 440 Hz, c'' = 532 Hz
    #     """plot fourrier transform"""
    #     #y = self.extract(channel,sampleBeginning,sampleEnd)
    #     try:
    #         xf, yf = self.fdata
    #     except AttributeError:
    #         xf, yf = self.transform(channel, sampleBeginning, sampleEnd, frequencyBeginning, frequency_end)

    #     plt.plot(xf, np.abs(yf)) #absolute value of fourrier transform
    #     plt.grid()
    #     plt.show()


    def findextrema(self, xf, yf,distance = 5,**kwargs):
        """
        returns: (xfPeaks, yfPeaks), dtype = np.array
        """

        if all(flag == 0 for flag in yf):
            return [0],[0]
        
        peaks, _ = find_peaks(yf, distance)    #indecies

        xfPeaks = xf[peaks]
        yfPeaks = yf[peaks]
        self.peaks = xfPeaks, yfPeaks
        return  xfPeaks, yfPeaks




class Translator():
    """used to transform the extracted frequencies into Notes"""
    def __init__(self):
        pass

    def translate(self, beginning, end):
        #frequencyToNoteValue
        pass


    def findMainFrequencies(self, xUnsorted , yUnsorted, threshhold = 1/3, number = 6, **kwargs):
        """returns:
            (x, y) of the last [number] datapoints
        """
        xUnsorted , yUnsorted

        # There are different ways to do a Quick Sort partition, this implements the
        # Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
        def partition(y, x, low, high):
            # We select the middle element to be the pivot. Some implementations select
            # the first element or the last element. Sometimes the median value becomes
            # the pivot, or a random one. There are many more strategies that can be
            # chosen or created.
            pivot = y[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while y[i] < pivot:
                    i += 1

                j -= 1
                while y[j] > pivot:
                    j -= 1

                if i >= j:
                    return j

                # If an element at i (on the left of the pivot) is larger than the
                # element at j (on right right of the pivot), then swap them
                y[i], y[j] = y[j], y[i]
                x[i], x[j] = x[j], x[i]


        def quick_sort(y,x):
            # Create a helper function that will be called recursively
            def _quick_sort(y, x, low, high):
                if low < high:
                    # This is the index after the pivot, where our lists are split
                    split_index = partition(y,x, low, high)
                    _quick_sort(y,x, low, split_index)
                    _quick_sort(y,x, split_index + 1, high)

            _quick_sort(y,x, 0, len(y) - 1)

        quick_sort(yUnsorted,xUnsorted)

        xSorted = list(np.flip(xUnsorted, -1))[:number]
        ySorted = list(np.flip(yUnsorted, -1))[:number]

            #TODO implement threshold 
        #if the peak is lower than 2/3 of the highest peak, delete it
        i = 0
        while i < len(ySorted):
            if ySorted[i] < ySorted[0]* threshhold:
                del ySorted[i]
                del xSorted[i]
            else:
                i += 1

        mainFrequencies = xSorted , ySorted #return the first [number] datatpoints

        return mainFrequencies
    

    def frequencyToNoteValue(self, frequency, fStartingNote = 440): #a=440 Hz
        """finds the note closest to the frequency"""
        if frequency == 0:
            return None
        n = 12 * np.log2(frequency/fStartingNote)    #see http://www.techlib.com/reference/musical_note_frequencies.htm 
        return int(round(n))


class Main(Extractor, Translator, Transformator):
    def __init__(self, file):
        Extractor.__init__(self, file=file)  #TODO initiate multi inherited class
    def _thread(self, data):
        """
        generator object
        input a song or a part of it
        used to implement a method for a ProcessPoolExecutor map(..)
        this is a convenience wrapper that brings together the different superclass methods
        returns:
            notes in the form of [[triad], [triad]...]
        """
        threshhold = 1/3
        NUMBER_OF_NOTES = 6
        transform = self.transform( y=data, frequencyBeginning = 300, frequencyEnd =  1000)
        mainFrequencies = self.findMainFrequencies(*self.findextrema(*transform, distance = 5), threshhold=threshhold, number=NUMBER_OF_NOTES )
        for i in mainFrequencies[0]:
            note = self.frequencyToNoteValue(i)
            yield note

    def split(self, splitLengthInSeconds, sampleBeginning, sampleEnd, channel = 0):


        data = self.extract(channel, sampleBeginning, sampleEnd)

        splitLengthInSeconds = 1
        numberOfSplits= int(round(self.lenght / (self.samplesPerSecond * splitLengthInSeconds)))
        print(f"numberOfSplits: {numberOfSplits}")  #TODO the number of splits dosnt seem to change with the split lenght
        return np.array_split(data, indices_or_sections= numberOfSplits )

    def thread(self, *args):
        """turns the _thread genrerator obj. into a list""" 
        return list(self._thread(*args))

    def main(self, chanel, sampleBeginning, sampleEnd, frequencyBeginning, frequencyEnd, distance, number, threshhold, fStartingNote = 440):
        self.values = self.extract(chanel, sampleBeginning, sampleEnd)
        self.xvalues = np.arange(sampleBeginning, sampleEnd, 1/self.samplesPerSecond)
        self.fvalues_xy = self.transform(self.values, frequencyBeginning, frequencyEnd)
        self.extrema = self.findextrema(*self.fvalues_xy, distance)
        self.mainFrequencies = self.findMainFrequencies(*self.extrema,threshhold, number)
        self.notes = list(map(lambda x: self.frequencyToNoteValue(x, fStartingNote), self.mainFrequencies[0]))
        return self.notes

    
if all((True, True, True == (True, True, True))):
    raise RuntimeError(f"""
    Broken Lines, broken strings,
    Broken threads, broken springs,
    Broken idols, broken heads,
    People sleeping in broken beds,
    Ain't no use jiving, 
    Ain't no use joking,
    EVERYTHING IS BROKEN
    for seriours: if you see this error, stop coding immediately, run and seek shelter in a nearby closet!
    """)