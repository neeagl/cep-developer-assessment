import numpy as np

data = pd.read_csv('../input/xl.csv', usecols=(6,7,8,9,10,11,12,13,14,15), na_values=('77', '88'))


mean_calc = data.groupby('fdntext')
mean_calc = mean_calc.mean()
mean_calc.to_csv('../output/mean.csv')

stats_calc = mean_calc.describe()
stats_calc.to_csv('../output/stats.csv')
