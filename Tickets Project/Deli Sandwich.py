sandwich_orders = ["Classic Sandwich", "Deli Sandwich", "Panini", "Shawarma Wrap"]
finished_sandwiches = []
while sandwich_orders:
    ordered_sandwiches = sandwich_orders.pop()
    print(f"Ordered sandwiches: {ordered_sandwiches}")
    finished_sandwiches.append(ordered_sandwiches)
print("")

print("The following are the completed sandwiches:")
for sandwich in finished_sandwiches:
    print(f" {sandwich.title()}")