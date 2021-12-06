# This is the python script to convert csv to grc readable format.  
# The csv is obtained using BitScope
import numpy as np
import csv
with open('BitScope.csv') as f:
	reader = csv.reader(f, delimiter=',')
	rate = []
	count = []
	dat = np.array([])
	dat1 = np.array([])
	data = np.array([])
	i=0
	for row in reader:
		dat = np.array(row[9:])
		if (i>0) :
			rate = float(row[7])
			count = int(row[8])
			dat1 = dat.astype(np.float)
			data=np.concatenate((data, dat1))
		i=i+1
newFile=open("test.dat","wb")
data.astype(np.float32).tofile(newFile)
