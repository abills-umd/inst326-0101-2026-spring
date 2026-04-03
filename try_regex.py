import re

def try_regex():
    expr = r"\w+"
    response = input("Give me a string: ")
    match = re.search(expr, response)
    print("The match is " + match[0] if match else "No match!")


if __name__ == "__main__":
    try_regex()
