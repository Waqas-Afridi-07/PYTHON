
line = 1
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes python is present, Line no:{lineno}")
        lineno += 1
        break
    else:
        print("Not present")