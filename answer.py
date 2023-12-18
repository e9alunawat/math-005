"""python that returns the smallest positive number 
that is evenly divisible by all of the numbers between 1 to 10"""
from solver import solver


def answer():
    """Base Condition"""
    return solver(1, 10)


if __name__ == "__main__":
    print(answer())
