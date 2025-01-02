# game_active = True
# if not game_active:
#     print("You are in a relaxing mode")
# else:
#     print("You are in a game session")

Id_present = True
correct_age = False
having_ATM = True

if Id_present and correct_age and not having_ATM:
     print("You cannot withdraw. You need an ATM card")
elif Id_present and correct_age and having_ATM:
    print("You can withdraw")
elif not Id_present and correct_age and having_ATM:
    print("You cannot withdraw. You need to an Id")
elif Id_present and not correct_age and having_ATM:
    print("You cannot withdraw. You should have over 18 years")
elif Id_present and correct_age:
    print("You can withdraw. Though it is only once!")
elif not Id_present and not correct_age and not having_ATM:
    print("Your withdrawal has been cancelled!")

else:
    print("Invalid requirements")

