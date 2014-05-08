
import numpy as np
from scipy.stats import percentileofscore
import csv

data = np.genfromtxt('../input/mean.csv', delimiter = ',', dtype=None)
size = data.shape[0]

myfile = open('../output/pct.csv', 'wb')
wr = csv.writer(myfile)
wr.writerow(data[0,])

percentile_questions_list= []
for i in range(0,size):
	if( i == 0 ):
		percentile_questions_list.append(data[1:size, i])
	else:
		rating_list=[]
		percentile_list = []
		rating_list = data[1:size, i]
		for r in rating_list:
			percentile = percentileofscore(rating_list, r, kind='mean')
			percentile_list.append(percentile)
		percentile_questions_list.append(percentile_list)

x = zip(*percentile_questions_list)
for r in x:
	row = []
	for t_item in r:
		row.append(t_item)
	wr.writerow(row)

