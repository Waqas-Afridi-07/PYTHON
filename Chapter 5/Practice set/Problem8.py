l = {}
print(type(l))

name = input("Enter friend's name : ") 
lang = input("Favorite language : ")

l.update({name: lang})

name = input("Enter friend's name : ") 
lang = input("Favorite language : ")

l.update({name: lang})

name = input("Enter friend's name : ") 
lang = input("Favorite language : ")

l.update({name: lang})

name = input("Enter friend's name : ") 
lang = input("Favorite language : ")

l.update({name: lang})

print(l)

# it'll return languages same because identifier's are keys in dictionary if they are same
# only last updated will be returned