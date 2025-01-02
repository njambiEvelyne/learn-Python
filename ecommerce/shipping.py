def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

def square(num):
    return int(num) * int(num)


print("Start")
greet_user(first_name=input("Enter first name: "), last_name= input("Enter last name: "))
ans =square(num = input("Enter a number: "))
print(ans)
print("Finish")