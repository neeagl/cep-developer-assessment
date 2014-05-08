
import numpy as np
from pandas import DataFrame
import pandas as pd
import json

meandata = np.genfromtxt('../input/mean.csv', delimiter = ',',  dtype=None)[9]
pctdata = np.genfromtxt('../input/pct.csv', delimiter = ',', dtype=None)[9]
statsdata = np.genfromtxt('../input/stats.csv', delimiter = ',', dtype=None)[4:9,]


question_list= ['fldimp','undrfld','advknow','pubpol','comimp','undrwr','undrsoc','orgimp','impsust']

question_dict = {}
for x in range(1, len(question_list)):
	question = {}
	question['type']='percentileChart'
	absolutesList = []
	for i in range(0,len(statsdata)):
		absolutesList.append(statsdata[i][x])
	question['absolutes']=absolutesList
	currentdict = {}
	currentdict['name']="2014"
	currentdict['value']=meandata[x]
	currentdict['percentage']=pctdata[x]
	question['current']=currentdict
	question['cohorts']=[]
	question['past_results']=[]
	question['segmentations']=[]
	question_dict[question_list[x]]=question

reports={"elements": question_dict, "segmentations": [], "cohorts": [], "name": "Tremont 14S Report", "title": "Tremont 14S Report"}
output_dict = {"version": "1.0",  "reports": [reports]}
#print output_dict

with open('../output/output.json', 'w') as outfile:
	json.dump(output_dict, outfile)
