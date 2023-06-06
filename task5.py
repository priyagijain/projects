# -*- coding: utf-8 -*-
"""task5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WG5pqylT1AfavKvVabbCNT3YQm7dyiTN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle

from google.colab import drive
drive.mount('/content/gdrive')

cd /content/gdrive/My Drive/Colab Notebooks/ML PRACTICAL/Logistic Regression/

columns = ['serial', 'TV','Radio','Newspaper','Sales'] 
df = pd.read_csv('ad.csv', names=columns)
df.head()

df

pip --version

pip install pandas_profiling

from pandas_profiling import ProfileReport

pf = ProfileReport(df)
pf.to_widgets()

#save this report

initialReport = pf.to_file('InitialReport.html')

#so we have to calculate y = mx+c from 200 data points
from sklearn.linear_model import LinearRegression

x = df[['serial']]
y = df.Sales

sns.pairplot(df, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=5, aspect=0.7)