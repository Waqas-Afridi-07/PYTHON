s = {4,1,7,9,11,"Waqas"}

s.add(43764736) # for adding values.
print(s)

s = {4,1,7,9,11,"Waqas"}
print(len(s)) # for getting length of set.

s = {4,1,7,9,11,"Waqas"}
s.remove("Waqas") # Removes specified elements.
print(s)

s = {4,1,7,9,11,"Waqas"}
s.pop() # removes a random element.
print(s)

s = {4,1,7,9,11,"Waqas"}
s.clear()
print(s)

s1 = {3,7,6}
s2 = {1,5,0,6,8}
print(s1.union(s2)) # union for both sets with non repetitive elements.

s1 = {3,7,6}
s2 = {1,5,7,6,0,8}
print(s1.intersection(s2)) # picks only similar values.