# import functions from niching space
from functions import shubert
from functions import vincent
from CF3 import CF3
from CF4 import CF4

# import other packages
import numpy as np
import csv

# filenames

shubert_file = "../../data/coords_shubert.csv"
vincent_file = "../../data/coords_vincent.csv"
cf3_file = "../../data/coords_CF3.csv"
cf4_file = "../../data/coords_CF4.csv"

# other globals

header_row = ["x", "y", "z", "fitness"]

# how many points to sample
pts = 1000

# ranges!

shubert_range = np.linspace(start=-10, stop=10, num=pts)
vincent_range = np.linspace(start = 0.25, stop=10.25, num=pts)
cf3_range = np.linspace(start=-5, stop=5, num=pts)
cf4_range = np.linspace(start=-5, stop=5, num=pts)
fcn_range = {"shubert": shubert_range, 
             "vincent": vincent_range,
             "CF3": cf3_range,
             "CF4": cf4_range}

# list the functions that we imported
# but we also need to know which ones need to be handled as classes
functions = [shubert, vincent, CF3, CF4]
classes = [CF3, CF4]

for fcn in functions:
    fname = "../../data/coords_" + fcn.__name__ + ".csv"
    frange = fcn_range[fcn.__name__]
    with open(fname, 'w') as fname:
        fcn_writer = csv.writer(fname, delimiter=",", quotechar='"')
        fcn_writer.writerow(header_row)
        for i in range(pts):
            x = y = z = frange[i]
            if fcn in classes:
                fitness = fcn(3).evaluate([x, y, z])
            else:
                fitness = fcn([x, y, z])
            fcn_writer.writerow([x, y, z, fitness])