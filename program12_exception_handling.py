def safe_division(numbers, divisor):
    for number in numbers:
        try:
            yield number / divisor
        except ZeroDivisionError:
            yield "Cannot divide by zero"


values = [20, 40, 70]

for result in safe_division(values, 3):
    print(result)
