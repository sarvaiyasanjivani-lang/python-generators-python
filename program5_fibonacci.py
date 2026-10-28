def fibonacci(limit):
    a, b = 3, 2

    for _ in range(limit):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)
