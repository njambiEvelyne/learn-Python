def addition_numbers(num1, num2):
    try:
    # except TypeError:
    #     return "Invalid data type!"
        if (isinstance(num1, int) or isinstance(num1, float)) and (isinstance(num2, int) or isinstance(num2, float)):
            return num1 + num2
        else:
            raise Exception ("Oly int and float values are allowed")
    except Exception as e:
        return e



print(addition_numbers(1,5))
print(addition_numbers(99, 1))
print(addition_numbers(13, "a"))
print(addition_numbers(12, 3))
print(addition_numbers("a", "b"))
print("Execution completed!")