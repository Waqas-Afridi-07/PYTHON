with open ("poem.txt") as f:

    content = f.read()
    if("Twinkle" in content):
        print("Twinkle is present.")

    else:
        print("Not present.")