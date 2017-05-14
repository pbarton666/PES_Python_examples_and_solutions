
import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities


#We could alternatively get data from a csv or Excel file pd.read_
filename='clean_polling_data.csv'
df=pd.read_csv(filename, dialect=None) #dialect defaults to Excel

#http://www.realclearpolitics.com/epolls/other/president_trump_job_approval-6179.html#polls
x=1

#****** a few useful operations ******

#shift all data by some number of periods
ser1=ser.shift(2)
printme(ser1)

ser1=ser.shift(-2)
printme(ser1)

#you can 'stretch out the index'
interval='18h'  #ms s m h d  are other options
ser1=ser.asfreq(interval)   
printme("Interval: " + interval, ser1)

ser1=ser.asfreq(interval, method='ffill')  #bfill is another
printme('Last value carried:', ser1)

ser.filter(items=[10,20])

ser=ser.sort_values(ascending=True)


index=pd.date_range(start='Jan 1 2017', end='Jun 5 2017')
data=list(range(len(index)))
ser=pd.Series(data=data, index=index)
x=1
#testing

#let's have a look
print (fmt2.format("Series:",ser))
printme("Index:",ser.index)

#append a new observation
ser=ser.append(pd.Series(data=[100], index=[pd.Timestamp('2/1/2017')]))
print(ser)
#read in some data
fn = 'polling_data.csv'
df=pd.read_csv(fn)

#use slicing to select subseries

all_2017=ser['2017']
print('\n everything')
print(all_2017)

feb_only=ser['2017-2']
print('\n February only')
print(feb_only)

jan1to3=ser['2017-1-1':'2017-1-3'] 
# same as ser.trunate(before='2017-1-1', after='2017-1-3')
print('\n first few days in January (note endpoints included)')
print(jan1to3)

#timestamps know a lot about themselves - a small sampling:
ts=feb_only.index[0]
print('\n',ts)
print("is it the end of the month?", ts.is_month_end)
print("what day of the year is it?", ts.dayofyear)
print("how many days in this month?", ts.daysinmonth)

#addition of a data point in Feb leaves gaps, so let's fill them in
new_index=pd.date_range(start=ser.index.min(), end=ser.index.max())
ser= ser.reindex(index=new_index)
print('\n', 'gaps filled in:')
print(ser)

#alternatively, we can prune the NaN rows
ser.dropna(how='any', inplace=True)
print('\n', 'NaN pruned', '\n')
print(ser)

#we can get rid of a row using drop() 
to_kill=ser.index[-1]
print('\n', 'killing', to_kill, '\n')
ser=ser.drop(to_kill)
print(ser)

#we'll add back a small gap and reindex
ser=ser.append(pd.Series(data=[100], index=[pd.Timestamp('1/10/2017')]))
new_index=pd.date_range(start=ser.index.min(), end=ser.index.max())
ser= ser.reindex(index=new_index)
print('\n', 'new series', '\n')

#... and do some stats
print('max is:', ser.max())
print('min is:', ser.min())
print('mean is:', ser.mean())
print('median is:', ser.median())
print('std is:', ser.std())

#do some on-the-fly manipulations
print('\n', "We can apply a function from numpy's library or roll our own")
print("Series.apply(<some_function>) does the trick") 
print('\n', 'here are the standardized values:')

#a lambda is an anonymous one-off function
mean=ser.mean()
std=ser.std()
print('\n', 'standardized', '\n')
print(ser.apply(lambda x: (x-mean)/std))

#do some scalar math
print('\n', 'add 500 to everything')
print(ser+500)

#display the data - lots of options here
chart=ser.plot.line()

#returns a figure object which we can play with
fig=chart.get_figure()
fig.set_tight_layout(True)
fig.show()

fig.savefig("myfigure.png")

chart=ser.plot.bar()
fig=chart.get_figure()
fig.set_tight_layout(True)
fig.show()

