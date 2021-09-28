import os
print(os.listdir())
print(os.curdir)
print(os.getcwd())
print(os.path.exists("a.txt"))
print(os.environ.get("PATH"))
os.makedirs("This/That")
print(os.path.join("C://", "/aakash"))
print(os.path.isfile("a.txt"))

import requests
url = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(url.text)
print(url.status_code)

import json
data = '{"var1": "harry", "var2":56, "var0":10000}'
print(type(data))
parsed = json.loads(data)
print(parsed)
print(type(parsed))
add = json.dumps(parsed, sort_keys=True, indent=4)
print(add)
print(type(add))

import pickle
li = ["Audi", "Bmw", "Toyota"]
f = open("cars.pkl", "wb")
pickle.dump(li, f)
f.close()

f = open("cars.pkl", "rb")
print(pickle.load(f))