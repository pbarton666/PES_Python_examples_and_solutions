#pandas_cluster_1

"""exploration classical 1936 R.A. Fisher dataset, demonstrates application of
   pandas and scikit-leart.  Data courtesy of:  
   http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
"""

import numpy as np              #python's array proccesing / linear algebra library
import pandas as  pd            #data processing / stats library
import matplotlib.pyplot as plt #data visualization
import matplotlib.dates as dates
import csv
import datetime
from py_utils import printme 	#home-made formatting utilities

file_name='iris_data.txt'
"""Data characterizes length and width of sepals and petals of Iris types.
   First couple of lines are:
      slength, swidth, plength, pwidth, class
	  5.1,3.5,1.4,0.2,Iris-setosa
"""
df=pd.read_csv(file_name)  #create a dataFrame object
x=1


