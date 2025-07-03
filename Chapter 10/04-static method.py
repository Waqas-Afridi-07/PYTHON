# it is a decorator and it doesnt use a self parameter

class Greet:
    @staticmethod
    def greet():
      print("Hello user")

Greet.greet()