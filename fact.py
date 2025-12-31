def factorial(num):
    fact = 1
    if num < 0:
        return None
    for i in range(1, num + 1):
        fact *= i
    return fact
