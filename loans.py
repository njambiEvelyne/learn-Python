high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan!")
else:
    print("Not Eligible")

has_chemistry = True
has_physics = False

if has_physics and has_chemistry:
    print("You are qualified for the course")
elif not has_physics or not has_chemistry:
    print("You are partially qualified. You have to bridge for Chemistry")
else:
    print("Not qualified")



