# just some anonymous function
from functools import reduce

mult = lambda x, y: x * y
print(mult(2, 7))

# lets put it to its intended use
points = [(0, 1), (1, 0), (0, 0), (-1, -1)]
print("sorted ", sorted(points, key=lambda x: x[1]))  # sortes by y

# similarly
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
c = [x * 2 for x in a]  # remember the good old way
print(list(b))

# likewise
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# finally
prod_a = reduce(lambda x, y: x * y, a)
print(prod_a)
