from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
x1 = [1,2,3]
y1 = [4,7,2]
x2 = [2,3,4]
y2 = [5,1,6]
plt.plot(x1, y1, "g", label="line one", linewidth=5)
plt.plot(x2, y2, "b", label="line two", linewidth=5)
plt.title("Distance-Time Graph")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.legend()
plt.grid(True, color="k")
plt.show()

plt.bar([1,3,5,7,9],[4,3,6,8,2], label="Python")
plt.bar([2,4,6,8,10],[3,2,7,2,5], label="Java", color="g")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Salary")
plt.title("Salary-Time Graph")
plt.show()

ages = [12,32,45,42,54,23,34,44,35,34,43,64,21]
bins = [10, 20, 30, 40, 50, 60, 70, 80]
plt.hist(ages, bins, histtype="bar", rwidth=0.8)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Title- Histogram")
plt.show()

x = [1,2,3,5,6,7]
y = [2,3,5,7,4,9]
plt.scatter(x, y, label='skitscat', color="k")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Title- Scatter Plot")
plt.legend()
plt.show()

days = [1,2,3,4,5]
sleep = [2,3,4,5,1]
eat = [5,6,7,8,9]
work = [5,6,7,8,6]
play = [1,2,1,2,1]
plt.plot([],[], color='m', label="sleep", linewidth=5)
plt.plot([],[], color='g', label="eat", linewidth=5)
plt.plot([],[], color='b', label="work", linewidth=5)
plt.plot([],[], color='c', label="play", linewidth=5)
plt.stackplot(days, sleep, eat, work, play, colors=['m','g','b','c'])
plt.legend()
plt.title("Days Schedule")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

slices = [7,2,2,13]
activities = ['sleep', 'eat', 'work', 'play']
cols = ['m','g','b','c']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
plt.show()

import numpy as np
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*2)

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)
plt.subplot(211)
plt.plot(t1, f(t1), 'o', t2, f(t2))
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()