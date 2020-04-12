from extractor import Extractor

extract = Extractor(r"528hz Pure tone No Music-IMeusltcDGM.wav")

import matplotlib.pyplot as plt
import numpy as np

print(extract.extract().__len__())
extract.plot(sample_beginning= 4,sample_end=5)