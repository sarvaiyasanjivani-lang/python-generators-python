def message_generator():
    try:
        yield "First message"
        yield "Second message"
    except ValueError:
        yield "ValueError handled inside generator"


gen = message_generator()

print(next(gen))
print(gen.throw(ValueError))
