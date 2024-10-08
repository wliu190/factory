import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

'''
This code is for simulating a virtual factory and predicting different properties of production.

In this factory making pins, there are four processes:
1. wire is cut
2. wire is straightened
3. pinhead is added
4. pin is sharpened

First, let's imagine a scenario where each steps precisely one second to complete.

Output
------
Number of produced pins against time
'''
    
def feed(count):
    t = 0
    return (t,count)

def operation(t, count, rate):
    # rate is per second
    t = t + 1/rate
    return (t, count)

def factory(time_run, feed_rate, cut_rate):
    time = 0.0
    count = 1

    cut_time = []
    cut_count = []

    while time < time_run:
        t, count = feed(count)
        t, count = operation(t, count, cut_rate)
        time = time + 1/feed_rate

        cut_time.append(time)
        cut_count.append(count)
        count = count + 1

    return cut_time, cut_count

x,y = factory(10, 1, 1)

plt.scatter(x,y)
plt.show()