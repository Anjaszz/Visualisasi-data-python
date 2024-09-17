# Penerapan konsep Measuring Asymmetric
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 #Mmebuat Grafik data histogram dengan matplotlib
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jumlah_kucing, bins=4)
plt.show()
 
# Parameter Skewness
jumlah_kucing_series = pd.Series(jumlah_kucing)
Skewness = jumlah_kucing_series.skew()
print("Nilai Skewness: " + str(Skewness))