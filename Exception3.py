def addition_numbers(num1, num2):

    try:
        answer = num1 + num2
        print(answer)
        return answer
    except TypeError:
        return "Invalid data type!"
    except Exception as e:
        return e
    # else:
    #     return "Succesfull"
    finally:
        print("The END")



addition_numbers(4, 6)
