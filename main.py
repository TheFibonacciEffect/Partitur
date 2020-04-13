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
        """ input: channel (mostly 1 or 0), beginning (seconds), end (seconds)

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
        #TODO do fourrier transform
        #how does the x axis need to look like in oder to give the right scale and make frequencies readable?

        # fft(x, n=None, axis=-1, norm=None, overwrite_x=False, workers=None)
        # Compute the one-dimensional discrete Fourier Transform.
        # Parameters
        # ----------
        # x : array_like
        #     Input array, can be complex.
        # n : int, optional
        #     Length of the transformed axis of the output.
        #     If `n` is smaller than the length of the input, the input is cropped.
        #     If it is larger, the input is padded with zeros.  If `n` is not given,
        #     the length of the input along the axis specified by `axis` is used.
        # axis : int, optional
        #     Axis over which to compute the FFT.  If not given, the last axis is
        #     used.
        # norm : {None, "ortho"}, optional
        #     Normalization mode. Default is None, meaning no normalization on the
        #     forward transforms and scaling by ``1/n`` on the `ifft`.
        #     For ``norm="ortho"``, both directions are scaled by ``1/sqrt(n)``.
        # overwrite_x : bool, optional
        #     If True, the contents of `x` can be destroyed; the default is False.
        #     See the notes below for more details.
        # workers : int, optional
        #     Maximum number of workers to use for parallel computation. If negative,
        #     the value wraps around from ``os.cpu_count()``. See below for more
        #     details.
        # Returns
        # -------
        # out : complex ndarray
        #     The truncated or zero-padded input, transformed along the axis
        #     indicated by `axis`, or the last one if `axis` is not specified.

        # Raises
        # ------
        # IndexError
        #     if `axes` is larger than the last axis of `x`.
        
        #fields 
        self.fdata = fft(x = self.data[:,channel], workers= -1) #complex value, __len__() = 300

        def plot(self):
            f = np.arange(0,300, self.samplesPerSecond)
            plt.plot(f, self.fdata)
            