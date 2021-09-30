import pandas as  pd
import plotly.figure_factory as ff
import statistics as stats
import random

dataset = []
df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

def random_set_of_data(counter):
    for i in range(0, counter):
        random_index = random.randint(0,(len(data) - 1))
        value = data[random_index]
        dataset.append(value)
    mean = stats.mean(dataset)
    return mean

def showfig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ['Temp'], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_data(100)
        mean_list.append(set_of_means)
    showfig(mean_list)
    mean = stats.mean(mean_list)
    print('Sampling Mean:- ', mean)
    std_dv = stats.stdev(data)
    print('Population Mean:- ', std_dv)

setup()