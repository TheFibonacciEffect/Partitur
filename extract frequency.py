class Extractor:
    """class used to extract a numpy array from a .wav file
    input:
        path to .wav
    output:
        numpy array (extract method)
    """
    def __init__(self, file):
        self.file = file
    def extract(self):
        pass #TODO https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
        # from scipy.io import wavfile
        # fs, data = wavfile.read('./output/audio.wav')