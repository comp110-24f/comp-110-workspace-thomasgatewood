"pracice with functions"
from random import randint

randint(1, 10)


def sum(num1: int, num2: int) -> int:
    """Return num1 + num2"""
    return num1 + num2


# Call the function
print(sum(num1=1, num2=10))  # <- 1 and 10 are arguments
# sum(num1=randint(1,10), num2=randint(2,20))
