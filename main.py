from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


class Extractor:
    """class used to extract a numpy array from a .wav file
    
    input:
        path to .wav
    
    methods:
        extract, returns the data as a np array
        plot(), plots it uning the matplotlib    
    """
    def __init__(self, file):
        self.file = file
        self.data = None
        fs, data = wavfile.read(self.file) #extract data
        self.samplesPerSecond = fs
        self.data = data    #type = matrix (sort of)
    def extract(self, channel = 0, beginning=0, end = -1):
        """input: channel (mostly 1 or 0), beginning (seconds), end (seconds)
        output: the data of the channel using a numphy array """
        beginning, end = int(beginning * self.samplesPerSecond), int(end * self.samplesPerSecond)
        self.data = self.data[:,channel][beginning:end]
        return self.data
    def plot(self, channel = 0,sample_end = None, sample_beginning = 0): #in seconds
        """ input: channel (std = 0), sample_end in seconds, sample_beginning in seconds
        plots the music using matplotlib, the self.extract() method will have to be called first """
        if sample_end == None:
            sample_end = self.extract(channel = 0).__len__() // self.samplesPerSecond
        
        x = np.arange(sample_beginning, sample_end, 1/self.samplesPerSecond) #start, stop, step

        #transform
        sample_beginning = int(sample_beginning * self.samplesPerSecond)
        sample_end = int(sample_end * self.samplesPerSecond) 
        sample_length = sample_end - sample_beginning

        y = self.data[:,channel][sample_beginning :sample_end]
        plt.plot(x,y)
        plt.show()

from scipy.fft import fft

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
        
    def transform(self,channel=0, sample_beginning=0, sample_end=-1, frequency_beginning = 55, frequency_end =  65, slicing = 1, chunks = 1):    #TODO change standard values to something reasonable
        """fourrier transforms given array, returns (xf,yf)
        slicing improves processing spead and memory usage
        returns:
            xf: x coordinate linspace
            yf: fourrier transform of input array"""
        #TODO feed data in chunks (maybe even read it in chunks, to impove memory usage?)
        y = self.extract(channel,sample_beginning,sample_end)[::slicing]    #increase slicing if MemoryError occours
        N = y.__len__()
        yf = fft(y, workers = -1) #workers = -1 is faster but will raise memory error #TODO when data is empty, raise exeption
        T = 1.0 / self.samplesPerSecond
        frequency_beginningIndex = int(frequency_beginning*T*N)
        frequency_endIndex = int(frequency_end*T*N)
        yf = yf[frequency_beginningIndex:frequency_endIndex]
        N = yf.__len__()
        xf = np.linspace(frequency_beginning, frequency_end, N)
        self.fdata = xf, np.abs(yf)
        return self.fdata


    def plot(self,channel=0,sample_beginning=0,sample_end=-1, frequency_beginning = 55, frequency_end =  65): #Low C = 130 Hz middle c = 261 Hz, a' = 440 Hz, c'' = 532 Hz
        """plot fourrier transform"""
        #y = self.extract(channel,sample_beginning,sample_end)
        try:
            xf, yf = self.fdata
        except AttributeError:
            xf, yf = self.transform(channel, sample_beginning, sample_end, frequency_beginning, frequency_end)

        plt.plot(xf, np.abs(yf)) #absolute value of fourrier transform
        plt.grid()
        plt.show()


    def findextrema(self,distance = 5,*args): #TODO implement  f_min, f_max
        """returns:
            (xfPeaks, yfPeaks), dtype = np.array"""
        try:
            xf, yf = self.fdata
        except AttributeError:
            xf , yf = self.transform(*args)
        
        peaks, _ = find_peaks(yf, distance)    #indecies
        
        
        xfPeaks = xf[peaks]
        yfPeaks = yf[peaks]
        return  xfPeaks, yfPeaks



class Translator(Transformator):
    def __init__(self, file, channel=0):
        super().__init__(file, channel=channel)
    def translate(self, beginning, end):
        #frequencyToNoteValue
        pass

    def frequencyToNoteValue(self, frequency, fStartingNote = 440): #a=440 Hz
        n = 12 * np.log2(frequency/fStartingNote)    #see http://www.techlib.com/reference/musical_note_frequencies.htm 
        return n

    def translateNote(self, note):
        """return character for note cloesest to given frequency eg. 440 -> a"""
        pass #https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
        