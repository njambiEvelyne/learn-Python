def addition_numbers(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        return "Invalid Number!"
    except NameError:
            return "Invalid parameter"
    except Exception as e:
        return e

print(addition_numbers(1,5))
print(addition_numbers(99, 1))
print(addition_numbers(13, "a"))
print(addition_numbers(12, 3))
print("Execution completed!")