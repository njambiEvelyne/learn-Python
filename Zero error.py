def division(digit1, digit2):
    try:
        return digit1 / digit2
    except ZeroDivisionError:
        return "Cannot divide the number by zero"


print(division(3, 0))
print(division(3,7))