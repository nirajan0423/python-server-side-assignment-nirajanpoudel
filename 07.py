# 7. Parse a JSON file representing product details (name, price, quantity) and display the
# details in tabular format

import json
from tabulate import tabulate

with open("practical/07_product.json", "r") as file:
    data = json.load(file)
    print(tabulate(data, headers="keys", tablefmt="simple_grid"))