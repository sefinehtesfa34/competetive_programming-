def decorator(func):
    def decorated():
        print("what is happening")
        func()
        print("What is happening now?")
    return decorated

@decorator
def plain():
    print("I don't know what it is.")
plain()