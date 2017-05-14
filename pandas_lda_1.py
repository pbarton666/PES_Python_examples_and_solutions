#pandas_lda_1
"""Linear Discriminant Analysis with pandas"""

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
from scipy.stats.mstats import normaltest
import matplotlib.pyplot as plt #data visualization
import seaborn as sns
import matplotlib.dates as dates #date munging
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities

live=False

"""
Use LDA when the dependent is categorical and independents are continuous.  Use
ANOVA when the situation is reversed.  It requires that the IVs are normally
distributed (not the case for logistical regression and probit.


"""

file_name='iris.data.csv'
"""Data characterizes length and width of sepals and petals of Iris types.
   First couple of lines are:
      slength, swidth, plength, pwidth, class
	  5.1,3.5,1.4,0.2,Iris-setosa
"""
#create a DataFrame object
df=pd.read_csv(file_name)
normal_results=normaltest(df['slength'])
plt.plot
a=1