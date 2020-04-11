from extractor import Extractor

extract = Extractor(r"Partitur\528hz Pure tone No Music-IMeusltcDGM.wav")

import matplotlib.pyplot as plt
import numpy as np

print(extract.extract().__len__())
extract.plot()