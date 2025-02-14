

from tabulate import tabulate

data = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Doctor"],
    ["Charlie", 28, "Artist"]
]

headers = ["Name", "Age", "Profession"]

print(tabulate(data, headers=headers, tablefmt="grid"))