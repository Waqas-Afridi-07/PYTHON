f = open("file2.txt")

lines = f.readlines() # .readline() reads only first line

print(lines, type(lines))

f.close