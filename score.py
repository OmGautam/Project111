import csv
import plotly.figure_factory as ff 
import pandas as pd 
import statistics
import random
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def randomSetMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanList = []
for i in range(0,1000):
    setOfMean = randomSetMean(100)
    meanList.append(setOfMean)

mean = statistics.mean(meanList)
print("Mean:",mean)
sd = statistics.stdev(meanList)
print("Standard Deviation:",sd)

first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean - (2*sd), mean + (2*sd)
third_sd_start, third_sd_end = mean - (3*sd), mean + (3*sd)

print("SD1:",first_sd_start, first_sd_end)
print("SD2:",second_sd_start, second_sd_end)
print("SD3:",third_sd_start, third_sd_end)

fig = ff.create_distplot([meanList],[mean],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0,17],mode = "lines", name = "mean"))

fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start], y=[0,0.17],mode = "lines", name = "sd1_start"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end], y=[0,0.17],mode = "lines", name = "sd1_end"))

fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start], y=[0,0.17],mode = "lines", name = "sd2_start"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end], y=[0,0.17],mode = "lines", name = "sd2_end"))

fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start], y=[0,0.17],mode = "lines", name = "sd3_start"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end], y=[0,0.17],mode = "lines", name = "sd3_end"))

fig.show()
