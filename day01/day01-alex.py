import pandas as pd
import numpy as np
import heapq

day01 = pd.read_excel("day01.xlsx")
cs = day01.apply(lambda x: x.groupby((np.isnan(x)).cumsum()).cumsum())

np.max(cs) # solution part 1 

sum(heapq.nlargest(3, cs["numbers"])) # solution part 2

