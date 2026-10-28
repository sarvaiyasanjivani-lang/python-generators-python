def count_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    


for number in count_numbers():
    print(number)
