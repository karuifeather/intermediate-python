from itertools import product, permutations, combinations, accumulate, groupby
from itertools import combinations_with_replacement as cwr
import operator
from itertools import count, cycle, repeat

# kinda like matrices, just kinda
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)

print(list(prod))

# permuatations return all possbile ordering of the tuple
c = [1, 2, 3]
p = permutations(c, 2)  # permuations with tuple with length 2
print(list(p))

# same but with combinations
com = combinations(c, 2)
print(list(com))

# combination with replacement
com = cwr(c, 2)
print(list(com))

# accumulation
x = [1, 2, 3, 4, 5, 6, 7]
print(x)
acc = accumulate(x)
print(list(acc))

# we can use it for other function such as multiplication
acc = accumulate(x, func=operator.mul)
print(list(acc))

# onto groupby
# next line specifically groups numbers into two groups that result true for the
# given condition
group_obj = groupby(x, key=lambda x: x > 3)

for key, value in group_obj:
    print(key, list(value))

# now, infinite loops

# this starts at 5 and keeps going
for i in count(5):
    print(i)

    if i == 10:
        break

# this keeps cycling through the list
y = [1, 2, 3, 4]

# for i in cycle(y):
#     print(i)

# this makes infinite loop by repeating the number
# you can also control how many times by passing a second argument
for i in repeat(1, 5):
    print(i)
