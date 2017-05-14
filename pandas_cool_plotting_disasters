
import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import matplotlib.dates as dates
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities

live=False

#create a new figure (high-level container)
plt.figure(figsize=(3,4), dpi=500, 
           facecolor='r', edgecolor='b')
plt.figure()
#add 'subplot' containers
rows=1; cols=2; plotnum=1  #subplots fill row-wise
plt.subplot(rows, cols, plotnum)
s1=pd.Series([np.sin(x/10) for x in range(0, 1200)])
red_circles='ro'
plt.plot(s1,red_circles )
#Create some data to be used in a time series