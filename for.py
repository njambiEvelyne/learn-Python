# prices = [10, 20, 30]
# total = 0
# for number in prices:
#     total +=number
# print(f"The total is {total}")
from Calculator import output

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

number = [5, 2, 5,2, 2]
for x_count in number:
     print("x "* x_count)
     print("")

#Alternatively
numbers = [1, 1, 1,1,7]
for x in numbers:
    output=""
    for count in range(x):
        output += "x"
    print(f"{output} " , "")

