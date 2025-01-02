# prices = [10, 20, 30]
# total = 0
# for number in prices:
#     total +=number
# print(f"The total is {total}")
from Lists import friends

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")
#
# number = [5, 2, 5,2, 2]
# for x_count in number:
#      print("x "* x_count)
#      print("")
#
# #Alternatively
# numbers = [1, 1, 1,1,7]
# for x in numbers:
#     output=""
#     for count in range(x):
#         output += "x"
#     print(f"{output} " , "")
#
squares = []
for value in range(1,21):
    square = value ** 2
    squares.append(square)
    print(squares)

# name = input("Enter your name: ")
# for char in name:
#     for x in range(1, 11):
#         print(f"{name}, {x}")
#         print("")

cost = [10,20,30,50,100]
print("\n")
print(sum(cost))

print("")
digits = list(range(1,11))

no = list(range(1,1000001))
print(no)
print("The sum is" , sum(no))

# num2 = list(range(1,21))
# for dig in num2:
#     if dig %2 != 0:
#         print(dig)
#         #print("These are the odd numbers")
# else:
#     print("The remaining are even numbers")

for num in range(1,31):
    if (num/3) == 0:
        print(num)
        print("These are the multiples of 3")
    else:
        print("Not multiples of 3")

my_foods = ["Pizza", "Chapati", "Chips"]
friends_foods = my_foods[:]
friends_foods.append("cake")
print(friends_foods)
print("")
print(friends_foods[1])

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

num = list(range (2, 10 ,2))
print(num)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)