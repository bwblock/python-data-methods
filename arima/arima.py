#! /usr/bin/env python

# code based on: https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/


from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv('sales-time.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)


# fit model  ---------  lag value 5, difference order 1, moving average model 0


model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())