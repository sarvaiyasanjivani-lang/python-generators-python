def running_total():
    total = 0

    while True:
        number = yield total
        if number is not None:
            total += number


gen = running_total()
print(next(gen))

print(gen.send(30))
print(gen.send(40))
print(gen.send(7))
