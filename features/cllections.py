# collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# this one used to count each chars repetitions
# returns a dict
counter = Counter("aashaya aryal")
print(counter)

# can get the most common elements like so
print(counter.most_common(2))  # two most common elements

# quick way to work with class
Point = namedtuple("Point", "x,y")
pt = Point(-2, 0)
print(pt)

# dict with an order
order_dict = OrderedDict()
order_dict["name"] = "Aashaya"

# default dict for when you got keys but no values
d = defaultdict(int)  # default data type int with value 0
d["name"] = "Aashaya"
d["age"] = 23
print(d["gender"])

# you can modify data from both ends using deque, list underneath
dq = deque()
dq.append(1)
dq.appendleft(0)
dq.append(2)

# [0,1,2]
print(dq)

# same with popping
print(dq.popleft())

# we also got extend or extendleft depending on the need
dq.extend([3, 4, 5, 6])
print(dq)

# another cool one is rotate
dq.rotate(2)
print(dq)
