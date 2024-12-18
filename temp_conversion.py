daily_temp_c =[1,3,5,8,45,3,10]

for temp_c in daily_temp_c:
    temp_faren = temp_c * (9/5) * 32
    print(f"The temperature in Farenheit is {temp_faren} ")

else:
    print("The conversion has been successful!")

names = ['Evelyne', 'Njambi', "Ng'ang'a"]
ages = [21, 12,13,51]

for names ,ages in zip(names, ages):
    print(f"The name is {names} with an age of {ages}.")
