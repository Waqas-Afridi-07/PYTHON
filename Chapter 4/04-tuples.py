# it is an unmutable data type version of a list in python

a = () # empty touple
print(a)

a = (1,) # a touple with only one element needs a comma otherwise python would consider it as an integer
print(a)

a = (5,7,3, "Rehan", 67.2, False) # proper touple with more than one element
print(a)

a [2] = 3
print(a) # output error "'tuple' object does not support item assignment"
