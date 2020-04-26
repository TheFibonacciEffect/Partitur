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
    def __init__(self, file, channel = 0):
        """gets values and fourrier transforms them"""
        super().__init__(file)
        #fields 
        self.fdata = fft(x = self.data[:,channel], workers= -1)

    def getTransform(self, ):
        pass #TODO put data generation into seperate method to make it able to be called inderpendendly
    def plot(self,channel=0,sample_beginning=0,sample_end=-1, frequency_beginning = 55, frequency_end =  65): #Low C = 130 Hz middle c = 261 Hz, a' = 440 Hz, c'' = 532 Hz
        
        y = self.extract(channel,sample_beginning,sample_end)
        # Number of sample points
        N = y.__len__()
        # sample spacing
        T = 1.0 / self.samplesPerSecond
        frequency_beginning = int(frequency_beginning*T*N)
        frequency_end = int(frequency_end*T*N)

        yf = fft(y)[frequency_beginning:frequency_end] #TODO Wie viel frequenz entspricht der Abstand zwischen zwei Datenpukten? N//2*1.0/(2.0*T)
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)[frequency_beginning: frequency_end] #start, stop, number of points : to cancel strech by linespacing,

        # plt.plot(xf[:-self.samplesPerSecond*29], 2.0/N * np.abs(yf[0:N//2][:-self.samplesPerSecond*29]))
        plt.plot(xf, np.abs(yf)) #absolute value of fourrier transform
        plt.grid()
        #plt.savefig(r"images\fourrier.png")
        plt.show()
            