from scipy.fft import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from os.path import isfile

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
            self.file = file
        else:
            self.file = file.replace("\\", "/" )    #UNIX uses foreward slashes instead of backslashes


    def extract(self, channel = 0, sampleBeginning =0, sampleEnd = -1):
        """input: channel (mostly 1 or 0), sampleBeginning (seconds), sampleEnd (seconds)
        output: the data of the channel using a numphy array """
        fs, data = wavfile.read(self.file) #extract data
        self.data = data
        self.samplesPerSecond = fs
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




class Transformator(Extractor):
    """Fourrier transforms given data
    inherits from Extractor
    methods:
        transform
        find extrema
        plot
    fields:
        fdata:  contains x and y coordinates of transformed data
    """

    def __init__(self, file):
        super().__init__(file)


    def transform(self, frequencyBeginning = 300, frequency_end =  1000, recalculateData = True, **kwargs):
        """the fourrier transform gives a representation of the frequencies in the input array
        fourrier transforms given array, returns (xf,yf)
        slicing improves processing spead and memory usage
        returns:
            xf: x coordinate linspace
            yf: fourrier transform of input array"""
        

        if recalculateData:
            y = self.extract(**kwargs)
        else:
            try: 
                y = self.data
            except AttributeError:
                y = self.extract(**kwargs)

        N = y.__len__()

        #TODO the chunking scales down the transform. This dosn't work.
        #chunk data & generate np.array

        yf = fft(y, overwrite_x=True)

        T = 1.0 / self.samplesPerSecond
        frequencyBeginningIndex = int(frequencyBeginning*T*N)
        frequency_endIndex = int(frequency_end*T*N)
        yf = yf[frequencyBeginningIndex:frequency_endIndex]
        N = yf.__len__()

        if all(flag == 0 for flag in yf):
            raise LookupError(f"""the array is empty (it only contains zeros) you need to determine a different beginning and end for the frequency
        here is the array: {yf} it's length is {yf.__len__()}, its shape is {yf.shape}""")

        xf = np.linspace(frequencyBeginning, frequency_end, N)
        self.fdata = xf, np.abs(yf)
        return self.fdata


    def plot(self,channel=0,sampleBeginning=0,sampleEnd=-1, frequencyBeginning = 55, frequency_end =  65): #Low C = 130 Hz middle c = 261 Hz, a' = 440 Hz, c'' = 532 Hz
        """plot fourrier transform"""
        #y = self.extract(channel,sampleBeginning,sampleEnd)
        try:
            xf, yf = self.fdata
        except AttributeError:
            xf, yf = self.transform(channel, sampleBeginning, sampleEnd, frequencyBeginning, frequency_end)

        plt.plot(xf, np.abs(yf)) #absolute value of fourrier transform
        plt.grid()
        plt.show()


    def findextrema(self,distance = 5,recalculateData = False,**kwargs):
        """if recalculateData, uses data from self.transform(**kwargs), otherwise self.fdata
        returns:
            (xfPeaks, yfPeaks), dtype = np.array"""

        if recalculateData:
            xf , yf = self.transform(**kwargs)
        else:
            try:
                xf, yf = self.fdata
            except AttributeError:
                xf , yf = self.transform(**kwargs)
        
        peaks, _ = find_peaks(yf, distance)    #indecies

        xfPeaks = xf[peaks]
        yfPeaks = yf[peaks]
        self.peaks = xfPeaks, yfPeaks
        return  xfPeaks, yfPeaks




class Translator(Transformator):
    """used to transform the extracted frequencies into Notes"""
    def __init__(self, file):
        super().__init__(file)


    def translate(self, beginning, end):
        #frequencyToNoteValue
        pass


    def findMainFrequencies(self, number, **kwargs):
        """takes the data from self.findextrema(**kwargs), and sorts it.
        returns:
            (x, y) of the last [number] datapoints
        """
        xUnsorted , yUnsorted = self.findextrema(**kwargs)

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

        self.mainFrequencies = xUnsorted[xUnsorted.__len__() - number:], yUnsorted[yUnsorted.__len__() - number:] #return the last five datatpoints

        return self.mainFrequencies
    

    def frequencyToNoteValue(self, frequency, fStartingNote = 440): #a=440 Hz
        n = 12 * np.log2(frequency/fStartingNote)    #see http://www.techlib.com/reference/musical_note_frequencies.htm 
        return n


    def translateNote(self, note):
        """return character for note cloesest to given frequency eg. 440 -> a"""
        pass #https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
        

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