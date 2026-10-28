def infinite_numbers():
    number = 3

    while True:
        yield number
        number += 3


gen = infinite_numbers()

for _ in range(10):
    print(next(gen))
