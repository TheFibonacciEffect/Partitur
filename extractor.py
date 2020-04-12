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
        self.data = data
    def extract(self, channel = 0):
        """ input: channel (mostly 1 or 0)
        output: the data of the channel using a numphy array """
        return self.data[:,channel]
    def plot(self, channel = 0,sample_end = None, sample_beginning = 0): #in seconds
        """ input: channel (std = 0), sample_end in seconds, sample_beginning in seconds
        plots the music using matplotlib, the self.extract() method will have to be called first """
        if sample_end == None:
            sample_end = self.extract(channel = 0).__len__() // self.samplesPerSecond
        
        x = np.arange(sample_beginning, sample_end, 1/self.samplesPerSecond) #start, stop, step

        #transform
        sample_beginning = sample_beginning * self.samplesPerSecond
        sample_end = sample_end * self.samplesPerSecond 
        sample_length = sample_end - sample_beginning

        y = self.data[:,channel][sample_beginning :sample_end]
        plt.plot(x,y)
        plt.show()

