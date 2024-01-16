# mutable, unordered, no duplicates

a = {1, 2, 3, 4, 2, 2, 2}
print(a)

# you can use it to find unique characters in the string
b = set("aashaya")
print(b)

# well, they are mutable so lets see how

# to add...
b.add(23)
b.add("M")
print(b)

# and to remove
b.remove("a")
print(b)

# a quirk with that one is that is throws error if the element isn't there; so
# when you want nothing to be done when no element is in the set
b.discard(140)

# you can also use clear to just get rid of everything like so
b.clear()

# other than that, pop and if x in set work the same way they do in lists
# next up, unions
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
print(evens.union(odds))

# as with set theory, there's intersection as well
# speaking of that, set itself works like sets in maths
primes = {2, 3, 5, 7, 11}
print(evens.intersection(primes))

# more on that: we got .difference() between two sets
a.difference(b)
print(a)

# updates itself with the union with another
odds.update(evens)
print(odds)

# along the lines of update: there is intersection_update and difference_update

# if you want something immutable, go for
c = frozenset([1, 2, 3, 4, 5])
