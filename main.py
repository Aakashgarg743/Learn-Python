print('Hello World')
print("Hello " * 10)
name = "aakash is the good boy"
print(" and ".join(name.split(" ")))
# Single Line Comment
# Multi Line Comment   - '''This also'''
'''
This is basically a docstring and tells that what a function is going to do
'''
# VARIABLES
x = 10
y = 10.234
z = 25j
a = True
print(x, y, z, a)
print(type(x), type(y), type(z), type(a))

# STRINGS
b = 'This is aakash'
print(type(b))
print(len(b))
print(b.title())
print(b.capitalize())
print(b.upper())
print(b.lower())
print(b.replace("aakash", "aakash garg"))
print(b[::2])
print(b[::-1])

# LIST
list1 = ["apple", "kiwi", "banana", "kiwi"]
print(list1)
print(type(list1))
print(len(list1))
print(list1[::-1])
print(list1.append("Orange"))
print(list1)
list1.reverse()
print(list1)

# DICTIONARY
role = {"Aakash": "Data Scientist",
        "Deepak": "Tester",
        "Rohan": "Developer"}
print(role)
print(role.keys())
print(role.values())
role["Manish"] = "Automation Tester"
print(role)

# TUPLE
tp = (1, )
print(tp)

# SETS
s = set()
print(type(s))
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)

# RANGE
print(list(range(11)))

# COLLECTIONS
from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict, UserList, UserString
a = namedtuple('courses', 'name, technology')
b = a("data science", 'python')
print(b)
s = a._make(['artificial intelligence', 'python'])
print(s)

a = ['a', 'a', 'k', 'a', 's', 'h']
d = deque(a)
print(d)
d.appendleft("mr.")
print(d)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
c = ChainMap(d1, d2, d3)
print(c)

a = [1,2,3,4,1,3,4,5,2,13,4,5,1,2,3,4,3]
c = Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub = {2:1, 13:1}
c.subtract(sub)
print(c)

d = OrderedDict()
d[1] = 'a'
d[2] = 'k'
d[3] = 'a'
d[4] = 's'
d[5] = 'h'
print(d)

d = defaultdict(int)
d[1] = "aakash"
d[2] = "garg"
print(d[3])

# ARRAYS
from array import *
a = array('i', [1, 2, 3, 4, 5, 6])
print(a)
print(a[3])
a[3] = 5
print(a)
print(len(a))
a.extend([1,2,3,4])
print(a)
print(a.pop())
print(a.remove(5))
print(a)
b = array('i', [1,2,3,4,5,6,7,8])
print(a+b)
for x in a:
    print(x)
print("----------------------")
i = 0
while i<len(a):
    print(a[i])
    i += 1

# LIST COMPREHENSIONS
val = [i for i in range(11) if i%2==0]
print(val)

# DICTIONARY COMPREHENSIONS
dict1 = {i:f"Item{i}" for i in range(5)}
val = {v:k for k, v in dict1.items()}
print(val)

# ONE LINE IF-ELSE
print("True") if 5>2 else print("False")

# HASHMAP AND HASHTABLE OR DICTIONARY
dic = dict(Aakash="Data Scientist", Manish="Tester")
print(dic)
# NESTED DICTIONARY
dic1 = {"employees": {"aakash":{"Id": 1, "surname": "garg", "salary": 2000000000, "Role":"Data Scientist"},
"manish":{"Id": 2, "surname": "kumar", "salary": 2000000, "Role":"Tester"}}}
print(dic1)

# DICTIONARY TO DATAFRAMES
from pandas import *
dic1 = {"employees": {"aakash":{"Id": 1, "surname": "garg", "salary": 2000000000, "Role":"Data Scientist"},
"manish":{"Id": 2, "surname": "kumar", "salary": 2000000, "Role":"Tester"}}}
df = DataFrame(dic1["employees"])
print(df)

# FILE HANDLING
import os
with open("a.txt", "w") as f:
    f.write("This is Aakash..")
with open("a.txt", "r+") as f:
    print(f.read())
    f.write("\nStarted Learning Python...\n")
with open("a.txt", "r") as f:
    print(f.tell())
    print(f.readline())
    f.seek(0)
    print(f.read())
if os.path.exists("b.txt"):
    os.remove("b.txt")
else:
    print("File doesn't exists..")

# FUNCTION - FIRST CLASS OBJECT - FUNCTION CAN BE PASSED TO ANOTHER FUNCTION AS AN ARGUMENTS
def fun(name):
    return f"Hello {name}"

def fun2(name):
    return f"{name}, How, you doing??"

def fun3(fun4):
    return fun4("Dear Learner")

print(fun3(fun))
print(fun3(fun2))

# INNER FUNCTION
def fun(n):
    def fun1():
        return "aakash"
    def fun2():
        return "python"
    if n==1:
        return fun1
    else:
        return fun2
a = fun(1)
b = fun(2)
print(a())
print(b())

# DECORATORS - EXAMPLE 1
def function1(function):
    def function2():
        print("Hello")
        function()
        print("This is from Aakash")
    return function2
@function1
def function3():
    print("pythonista")
# function3 = function1(function3)
function3()

# DECORATORS - EXAMPLE 2
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    @property
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return "Email is not set..."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    @staticmethod
    def stmeth(name):
        return f"Hello {name}"

aakash = Employee("aakash", "garg")
print(aakash.explain)
print(aakash.email)
aakash.fname = "manish"
print(aakash.email)
aakash.email = "this.that@gmail.com"
print(aakash.fname)
print(aakash.email)
print(aakash.stmeth("aakash"))
del aakash.email
print(aakash.email)

# LAMBDA OR ANONYMOUS FUNCTIONS
v = lambda a:a*a
print(v(3))

def A(x):
    return lambda y:x+y
a = A(3)
print(a(4))

# MAP - apply a given function to all iterables and return a new list
mylist = ["1", "2", "3", "4"]
new = list(map(int, mylist))
new[0] = new[0]+1
print(new)

# REDUCE
from functools import reduce
mylist = [1,2,3,4,5,6,7]
new = reduce(lambda a, b:a+b, mylist)
print(new)

# FILTER    - filter is used to filter an expression that whether a expression is going to be true or false
mylist = [1,2,3,4,5,6,78,8]
new = list(filter(lambda a:(a/3==2), mylist))
print(new)

# FILTER WITH MAP
new = map(lambda x:x+x, filter(lambda a:a>=3, [1,2,3,4,5,6]))
print(list(new))

# MAP AND FILTER WITH REDUCE
new = reduce(lambda x, y:x+y , map(lambda z:z+z, filter(lambda a:a>3, [1,2,3,4,5])))
print(new)

# GENERATORS
def myfun(a):
    for k, v in a.items():
        yield k, v
a = {1:"Aakash", 2:"Manish"}
b = myfun(a)
print(a)
print(next(b))

# FIBONACCI SERIES - 0, 1, 1, 2, 3, 5, 8, 13
def fib(n):
    a = 0
    b = 1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
print(fib(6))

n = int(input("Enter a number: \n"))
a = 0
b = 1
if n==1:
    print("0")
elif n==2:
    print("1")
else:
    print("0")
    print("1")
    for i in range(2, n):
        a, b = b, a+b
        print(b)

# EXCEPTION HANDLING
a = 10
b = 0
try:
    c = a/b
except Exception as e:
    print(e)
else:
    print("This only runs when except is not running...")
finally:
    print("This is always printed...")

# RECURSION
def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)
n = int(input("Enter a number:\n"))
print(facto(n))

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
f = fibo(15)
print(f)

# SCOPE
a = 10
def fun():
    global a
    a = 20
    print(a)
fun()
print(a)

# *ARGS AND **KWARGS
def funciton1(n, *args, **kwargs):
    print(n)
    for i in args:
        print(i)
n = "aakash"
l1 = ["aakash", "manish", "rohan", "nakul"]
dic = {"name":"aakash", "id":1, "score":1000}
funciton1(n, *l1, **dic)

# ENUMERATE
l1 = ["aakash", "manish", "nakul", "rohan"]
for i, v in enumerate(l1):
    if i%2==0:
        print(v)

# CLASSES AND OBJECTS - OOPS CONCEPT
class Employee:
    leaves = 10
    def __init__(self, fname, lname, age, gender):
        self._fname = fname
        self._lname = lname
        self._age = age
        self._gender = gender

    def print_details(self):
        return self._fname + self._lname + self._age + self._gender

    @classmethod
    def change_leaves(cls, new_leave):
        cls.leaves = new_leave

    @classmethod
    def get_details(cls, string):                            # - ALTERNATIVE CONSTRUCTOR
        new = string.split("-")
        return cls(new[0], new[1], new[2], new[3])

e1 = Employee("aakash ", "garg ", "22 ", "male ")
e2 = Employee.get_details("manish-kumar-22-male")
print(e1.print_details())
e1.change_leaves(20)
print(e1.__dict__)
print(Employee.leaves)
print(e2.__dict__)

# ABSTRACT CLASS
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def dim(self, len, bre):
        pass

class Rectangle(Shape):
    def dim(self, len, bre):
        self._len = len
        self._bre = bre

    def area(self):
        return self._len*self._bre
s = Rectangle()
s.dim(20, 40)
print(s.area())

# TIME
import datetime
print(datetime.datetime.now())
print(datetime.date.today())

import time
print(time.time()) #- provides seconds from ephoc time
print(time.ctime(1632473531.3418422)) # - convert seconds into the today's time
print(time.localtime()) # - struct_time and for convert this - use asctime
print(time.gmtime())
print(time.mktime())
print(time.asctime())

# MATPLOTLIB
import matplotlib.pyplot as plt
plt.bar([0.25, 1.25, 2.25, 3.25, 5.75], [50,40,70,80,20], label="Python", color="red", width=.3)
plt.bar([1, 2, 3, 4, 5], [40,30,50,60,10], label="Java", color="blue", width=.3)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Marks')
plt.title('Information')
plt.show()

days = [1,2,3,4,5]
sleeping = [7,6,5,4,2]
eating = [8,7,6,4,5]
working = [5,4,3,2,1]
slices = [7,2,2]
cols = ['c', 'm', 'g']
activites = ['sleeping', 'eating', 'working']
plt.pie(
    slices, labels=activites, colors = cols, shadow=True, explode=(0,0.2,0), autopct='%1.1f%%'
)
plt.title('Pie Plot')
plt.show()

# GENERATE SINE WAVES
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
def s(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sb.set()
s()
plt.show()

# REGULAR EXPRESSION
import re
str = '''Regular Expressions | Python Tutorials For Absolute Beginners In Hindi #86
68-434 views6 Jan 2019
2.2K
82
SHARE
aakashgarg@gmail.com
aakash.garg@gmail.co.in
aak_garg.coder@micro.ac.in
SAVE
CodeWithHarry
1.88M subscribers
►Source Code + Text Tutorial - https://www.codewithharry.com/videos/...
►Full Python tutorials for absolute beginners (Hindi) playlist - https://www.youtube.com/playlist?list...
►Click here to subscribe - https://www.youtube.com/channel/UCeVM...
Best Hindi Videos For Learning Programming:
►Learn Python In One Video - https://www.youtube.com/watch?v=qHJjM...
►Learn JavaScript in One Video - https://www.youtube.com/watch?v=onbBV...
►Learn PHP In One Video - https://www.youtube.com/watch?v=xW7ro...
►Machine Learning Using Python - https://www.youtube.com/playlist?list...
►Creating & Hosting A Website (Tech Blog) Using Python - https://www.youtube.com/playlist?list...
►Advanced Python Tutorials - https://www.youtube.com/playlist?list...
►Object Oriented Programming In Python - https://www.youtube.com/playlist?list...
►Python Data Science and Big Data Tutorials - https://www.youtube.com/playlist?list...
Follow Me On Social Media
►Website (created using Flask) - https://www.codewithharry.com
►Facebook - https://www.facebook.com/CodeWithHarry
►Instagram - https://www.instagram.com/codewithharry/
►Personal Facebook A/c - https://www.facebook.com/geekyharis
Twitter - https://twitter.com/Haris_Is_Here
342 Comments
Aakash Garg
Commenting publicly as Aakash Garg
Aman Patel
Aman Patel
11 months ago
thank you harry bhaiya for teaching us codes in free, we will remember you for whole life'''

# patt = re.compile(r'Aakash')
# patt = re.compile(r'\d{2}-\d{3}')
patt = re.compile(r'[A-Za-z0-9.+_%]+@[A-Za-z0-9.+_%]+[.][A-Za-z.0-9]+')
new = patt.finditer(str)
for i in new:
    print(i)