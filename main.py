from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


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
        """ 
        input: channel (mostly 1 or 0), beginning (seconds), end (seconds)
        output: the data of the channel using a numphy array """
        beginning, end = int(beginning * self.samplesPerSecond), int(end * self.samplesPerSecond)
        return self.data[:,channel][beginning:end]
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
    def __init__(self, file):
        """gets values and fourrier transforms them"""
        super().__init__(file)
        
    def transform(self,channel=0, sample_beginning=0, sample_end=-1, frequency_beginning = 55, frequency_end =  65):
        y = self.extract(channel,sample_beginning,sample_end)
        N = y.__len__()
        yf = fft(y)
        T = 1.0 / self.samplesPerSecond
        frequency_beginning = int(frequency_beginning*T*N)
        frequency_end = int(frequency_end*T*N)
        return yf[frequency_beginning:frequency_end]
    def plot(self,channel=0,sample_beginning=0,sample_end=-1, frequency_beginning = 55, frequency_end =  65): #Low C = 130 Hz middle c = 261 Hz, a' = 440 Hz, c'' = 532 Hz
        """plot fourrier transform"""
        #y = self.extract(channel,sample_beginning,sample_end)
        
        yf = self.transform(channel, sample_beginning, sample_end, frequency_beginning, frequency_end)
        
        #nr. sample points
        samplePoints = yf.__len__()
        xf = np.linspace(frequency_beginning, frequency_end, samplePoints) #start, stop, nr. segments
        plt.plot(xf, np.abs(yf)) #absolute value of fourrier transform
        plt.grid()
        plt.show()

class Translator(Transformator):
    def __init__(self, file, channel=0):
        super().__init__(file, channel=channel)
    def translate(self, beginning, end):
        pass

    def frequencyToNoteValue(self, frequency, startingNote = 440): #a=440 Hz
        n = 12 * np.log2(frequency/startingNote)    #see http://www.techlib.com/reference/musical_note_frequencies.htm 
        return n
    def translateNote(self, note):
        """return key of note cloesest to given frequency eg. 441 -> a"""
        pass #https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value