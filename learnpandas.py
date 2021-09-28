import pandas as pd
web = {"Day": [1,2,3,4,5,6], "Visitors": [1000,7000, 600, 100, 240, 5000], "Bounce_Rate":[20, 20, 10, 43, 20, 40]}
df = pd.DataFrame(web)
print(df)

# SLICING
print(df.head(2))
print(df.tail(2))

# MERGING
df1 = pd.DataFrame({"Name": ["Aakash", "Manish", "Shubham", "Rohit"], "Salary":[10000,100,10,1], "Houses":[5,4,3,2]})
df2 = pd.DataFrame({"Name": ["Aakash", "Manish", "Deepak", "Kishan"], "Salary":[10000,100,10,1], "Houses":[5,4,3,2]})
new = pd.merge(df1, df2,  on="Salary")
print(new)

# JOINING
# df1 = pd.DataFrame({"Salary":[2100,3100,2340,3000]}, index=[1,2,3,4])
# df2 = pd.DataFrame({"Cars":[21,31,34,3]}, index=[1,3,4,4])
# new = df1.join(df2)
# print(new)

# CHANGE THE INDEX AND COLUMN HEADERS
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df = pd.DataFrame({"Day":[1,2,3,4], "Visitors":[233,323,325,31], "Bounce_Rate":[21,34,65,43]})
print(df)
df.set_index("Day", inplace=True)
print(df)
df.plot()
plt.show()
df = df.rename(columns={"Visitors":"Users"})
print(df)

# CONCATENATION
# df1 = pd.DataFrame({"Name":["Aakash", "Manish", "Rohit", "Shubham"], "Age":[21,34,21,35], "Sex":["Male", "Male", "Male", "Male"]}, index=[1,2,3,4])
# df2 = pd.DataFrame({"Name":["Aakash", "Manish", "Rohit", "Shubham"], "Age":[21,34,21,35], "Sex":["Male", "Male", "Male", "Male"]}, index=[5,6,7,8])
# con = pd.concat([df1, df2])
# print(con)

# DATA MUNGING
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
df = pd.read_csv(url, names=names)
new = pd.DataFrame(df)
sd = df.reindex(columns = ['sepal-length', 'sepal-width'])
print(new)
print(sd)
df.to_html('iris_html')

# STATISTICS
from statistics import mean, median, mode, median_low
print(mean([1,2,3,4]))
print(median([1,2,3,4]))
print(median_low([1,2,3,4]))
print(mode([1,23,4,4,4,2,3,4]))