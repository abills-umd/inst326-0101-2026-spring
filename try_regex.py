import re

def foo()
    print("Hello! This is Jong's code")

def try_regex_othername():
    expr = r"\w+"
    print("This is Jong's code")
    print("This is Jong's code")
    response = input("Give me a string: ")
    match = re.search(expr, response)
    print("The match is " + match[0] if match else "No match!")

    print("This is Jong's code")
    print("I'm doing useless print statements here because I'm not good at regex")


if __name__ == "__main__":
    try_regex_othername()
