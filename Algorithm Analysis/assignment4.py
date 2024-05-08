import math
import numpy as np
import matplotlib.pyplot as plt

for msize in [5, 15, 50]:
  n = np.arange(0, msize, 0.1)

  plt.plot(n, (2**10)*n + 2**10 , 'red', n, n**3.5 - 1000, 'blue', n, 100*n**2.1 + 50, 'green')

  plt.xlim(0, msize)
  plt.rcParams["figure.figsize"] = (7,7)
  plt.show()
 



