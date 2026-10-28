def colours():
    yield "Red"
    yield "Black"


def flowers():
    yield "Rose"
    yield "Sunflower"


def all_colours():
    yield from colours()
    yield from flowers()


for colour in all_colours():
    print(colour)
