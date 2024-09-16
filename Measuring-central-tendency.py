
import numpy as np
from scipy import stats

all_cat = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
print(f"Data : {all_cat} " )
#Mean
mean_cat = all_cat.mean()
print(f"mean dari data diatas : {mean_cat}")
#median
median_cat = np.median(all_cat)
print("Median dari data diatas : " + str(median_cat))

#mode
mode_allcat = stats.mode(all_cat)[0]
print("Mode dari data diatas : " + str(mode_allcat))