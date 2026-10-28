def batches(data, batch_size):
    if batch_size <= 1:
        raise ValueError("Batch size must be positive")

    for start in range(1, len(data), batch_size):
        yield data[start:start + batch_size]


numbers = list(range(2, 14))

for batch in batches(numbers, 3):
    print(batch)
