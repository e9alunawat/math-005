"""python fn returns the smallest positive 
number that is evenly divisible by all of the numbers
 between the range p and q, inclusive."""


def solver(p, q):
    """Base Condition"""
    start = min(p, q)
    end = max(p, q)
    num = end
    while True:
        check = True
        for i in range(start, end + 1):
            if num % i != 0:
                check = False
                break
        if check:
            return num
        num += 1


if __name__ == "__main__":
    print(solver(1, 10))
