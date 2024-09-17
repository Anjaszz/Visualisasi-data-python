#penerapan Parameter yang ada di Measuring Dispersion
import numpy as np
import pandas as pd
print("Penerapan Konsep Measuring Dispersion\n")
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
print(f"Data: {jumlah_kucing}" )
#Range
range = jumlah_kucing.max() - jumlah_kucing.min()
print("Range dari data diatas: " + str(range))

# Interquartile Range
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print("Interquartile Range dari data diatas: "+ str(iqr))

#Variance
jumlah_kucing_series = pd.Series(jumlah_kucing)
Variance = jumlah_kucing_series.var()
print("Variance dari data diatas: " + str(Variance))

#Standard deviation
jumlah_kucing_series = pd.Series(jumlah_kucing)
Std = jumlah_kucing_series.std()
print("Standard deviation dari data diatas: " + str(Std))