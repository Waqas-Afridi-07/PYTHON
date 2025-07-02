with open ("file 5.txt", "w") as f :

    text = f.write("Hello")

    print(text)

# we don't have to write .close() function while using with statement