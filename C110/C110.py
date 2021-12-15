import csv
from os import stat
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd


df=pd.read_csv("data110.csv")
data=df["temp"].tolist()
mean=statistics.mean(data)
std=statistics.stdev(data)
print("Mean of the data",mean)
print("Standard deviation of the data",std)
fig=ff.create_distplot([data],["Temperature"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1],mode="lines",name="MEAN"))
fig.show()