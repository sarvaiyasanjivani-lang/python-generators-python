def read_file_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


# Create a sample file
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python Generators\n")
    file.write("Advanced Python\n")
    file.write("Memory Efficient Programming\n")


for line in read_file_lines("sample.txt"):
    print(line)
