import random
import plotly.express as px 
import plotly.figure_factory as ff 
import statistics

dice_result = []
for i in range(0,1000):
        dice1 = random.randint(0,6)
        dice2 = random.randint(0,6)
        dice_result.append(dice1 + dice2)

mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
print('Mean of the data: ' + str(mean))
print('Standard deviation: ' + str(std_deviation))
print('Median of the data: ' + str(median))
print('Mode of the data: ' + str(mode))
fig = ff.create_distplot([dice_result],['Result'],show_hist=False)
fig.show()
