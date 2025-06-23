marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.items()) # returns (key, value) pairs in the form of "tuples".

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}
print(marks.keys()) # returns dictionary keys.

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.values()) # returns values of keys.

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.update({"Waqas" : 45 })) # for updating the original dictionary because it is mutable.
print(marks)

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.clear()) # for clearing dictionary.
print(marks)

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.copy()) # for creating a shallow copy.
print(marks)

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.pop("Ibrar")) # it removes the specified key from the dictionary and returns its value.
print(marks)

marks = {
    "Waqas" : 23,
    "Ibrar" : 87,
    "Nasir" : 100
}

print(marks.popitem()) # removes the last key value pair added to the dictionary.
print(marks)