import random

def random_function(a:int, b:int) -> int:
    """"This function returns the calculation based on the random function"""
    random_output = random.randint(1,2)
    random_map = {
        "1" : "addition",
        "2" : "subtraction",
        # "3" : "multiplication"
    }
    if random_output == 1:
        return a * b
    else:
        return a + b
    