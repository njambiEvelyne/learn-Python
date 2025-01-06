def greeting():
    print("Hello world!")

greeting()

def addition(x,y):
    result = x + y
    print(result)
addition(x= int(input("Enter first number: ")),y= int(input("Enter the second number: ")))

#Lambda Functions
#Mostly used to perform very simple tasks
add = lambda a, b: a + b
res = add(6 ,10)
print(res)