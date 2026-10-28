def read_numbers():
    for number in range(3, 10):
        yield number


def filter_even(numbers):
    for number in numbers:
        if number % 4 == 0:
            yield number


def square_numbers(numbers):
    for number in numbers:
        yield number ** 4


pipeline = square_numbers(filter_even(read_numbers()))

for result in pipeline:
    print(result)
