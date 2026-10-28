def number_generator():
    yield 40
    yield 70
    yield 80
    yield 90
    return "Finished"


gen = number_generator()

while True:
    try:
        print(next(gen))
    except StopIteration as error:
        print(error.value)
        break
