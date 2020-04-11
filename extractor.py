from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


class Extractor:
    """class used to extract a numpy array from a .wav file
    input:
        path to .wav
    output:
        numpy array (extract method)
    """
    def __init__(self, file):
        self.file = file
        self.data = None
    def extract(self, channel = 0):
        fs, data = wavfile.read(self.file)
        self.samples = fs
        self.data = data
        return self.data[:,channel]
    def plot(self, channel = 0,sample_length = None):
        if sample_length == None:
            sample_length = self.extract(channel = 0).__len__()
        y = self.data[:,channel][:sample_length]
        x = np.arange(0,sample_length * 1/ self.samples,1/self.samples)
        plt.plot(x,y)
        plt.show()

