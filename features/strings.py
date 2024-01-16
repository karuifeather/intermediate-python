# strings are ordered and immutable
# accessing works like lists

# here's a trick to reverse tho
text = "aashaya"
print(text[::-1])

# and here's a fun one
guess_what = "hello world!!"
print(guess_what.replace("world", "ash"))

# you can build them from list of strings
another = "".join(["a", "b", "c", "d"])
print(another)

# conversely you can split it like so
print(another.split())
# note unlike with list(), it does not split down to its chars
# you need a delimiter [default is " "]

# next up is formatting strings
name = "Ash"
big_text = "Hi, you can call me %s" % name
print(big_text)
# for decimal %d
# for floats %f
# for floats with specified digits %.2f

# there's newer way to do this, with .format
example = "my name my name, {} and {:.2f}".format("chika chika", 3.141527)
print(example)

# now, the latest way of doing it, with f-strings
some_num = 3.141527
another_text = f"value is {some_num:.3f}"
print(another_text)
