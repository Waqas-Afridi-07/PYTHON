# There are different types of methods.

numbers = [1,6,4,9,3,8,0,2]
numbers.sort() # for arranging list in a proper order
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.reverse() # for reversing list
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.append(5) # adds user entered value at the "end" of string
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.insert(5,10) # inserts elements of the user's will 
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.pop(2) # for deleting element at user given index
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.remove(8) # removes user given "elements"
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.extend([1,9])
print(numbers)

numbers = [1,6,4,9,3,8,0,2]
numbers.clear() # removes all elements
print(numbers)

numbers = [1,6,6,6,4,9,3,8,0]
print(numbers.count(6)) # for counting elements

numbers = [1,6,4,9,3,8,0,2]
print(numbers.index(4))