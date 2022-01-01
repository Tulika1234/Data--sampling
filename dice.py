import random
import plotly.express as px
import statistics 
import plotly.figure_factory as ff
import plotly.graph_objects as go


count = []
diceResult = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)

average = sum(diceResult)/len(diceResult)
stDev = statistics.stdev(diceResult)
median1 = statistics.median(diceResult)
mode1  = statistics.mode(diceResult)

first_std_deviation_start, first_std_deviation_end = average-stDev, average+stDev
second_std_deviation_start, second_std_deviation_end = average- (2*stDev), average+(2*stDev)
third_std_deviation_start, third_std_deviation_end = average- (3*stDev), average+(3*stDev)



fig = ff.create_distplot([diceResult],['Result'],show_hist = False)
fig.add_trace(go.Scatter(x= [first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name = 'FIRST STD'))
fig.add_trace(go.Scatter(x= [first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name = 'FIRST STD'))

fig.add_trace(go.Scatter(x= [second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name = 'SECOND STD'))
fig.add_trace(go.Scatter(x= [second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name = 'SECOND STD'))

fig.add_trace(go.Scatter(x= [third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode='lines',name = 'THIRD STD'))
fig.add_trace(go.Scatter(x= [third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode='lines',name = 'THIRD STD'))


fig.show()




print("This is the mean:",average)
print("This is the standard deviation:",stDev)
print("This is the median of the result:", median1)
print("This is the mode of the results:", mode1)