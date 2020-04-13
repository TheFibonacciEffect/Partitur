from scipy.fft import fft
import numpy as np
from main import Extractor

extract = Extractor(r"60 Hz Test Tone-GqwFimG3X3w.wav")
# Number of sample points
N = extract.extract(beginning=0, end=-1).__len__()
# sample spacing
T = 1.0 / extract.samplesPerSecond

y = extract.extract()
x = np.linspace(0.0, N*T, N) #start, stop, nr
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2) #start, stop : to cancel strech by linespacing,
import matplotlib.pyplot as plt

plt.plot(x,y)
plt.grid()
#plt.show()
#plt.savefig(r"images\osszilation.png")
plt.clf()


plt.plot(xf[:-extract.samplesPerSecond*29], 2.0/N * np.abs(yf[0:N//2][:-extract.samplesPerSecond*29]))
plt.grid()
#plt.savefig(r"images\fourrier.png")
plt.show()

