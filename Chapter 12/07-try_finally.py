def main():
    try:
     a = int(input("Hey, Enter a number : "))
     print(a)
     return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside of finally") # A function will only execute if it's called.
                                        # If there’s an error before the call, the function won’t run.
                                        # The finally block always runs, whether an error occurs or not.

main()