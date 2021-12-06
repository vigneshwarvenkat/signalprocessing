# Use csv2grcf.py to extract csv data to python binary data stored in "test.dat" and "time.dat"
# Then use this script to read from "test.dat" and "time.dat", and create the PWL file readable by LTSPICE for simulation

import numpy as np

t=np.fromfile("timef_spice.dat",np.float32)
data=np.fromfile("testf_spice.dat",np.float32)

data1=np.vstack((t,data)).T

np.savetxt('sig1.dat', data1, fmt='%.16e', delimiter=',', newline='\n', header='', footer='', comments='#')

