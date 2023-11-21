counter = 0

with open('change_log.txt', 'r') as file:
    lines = file.readlines()
    for line_number, line in enumerate(lines, start=1):
        if line.startswith("2"):
            counter += 1

    print(f"-- Found {counter} Classes that implement 'Super'")