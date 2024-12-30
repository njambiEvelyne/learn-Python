friends= ["Jane", "Solomon", "Mwikali", "Rose", "Grace"]
print(friends)
friends[3]= "Rodah\n"
print(friends[3])

cool=["Evelyne", "Cole", "Jasmine"]
lucky_Numbers= [4,5,7,79,14]
print(cool)
print("\nExtend can be used to add on to a list\n")
cool.extend(lucky_Numbers)
print(cool)

cool=["Evelyne", "Cole", "Jasmine"]
lucky_Numbers= [4,5,7,79,14]
print(cool)
print("\nAppend allows one to add items that at=re needed\n")
cool.append("Creed")
print(cool)

cool=["Evelyne", "Cole", "Jasmine"]
lucky_Numbers= [4,5,7,79,14]
print(cool)
print("\nInsert allows on to insert an object at a given index\n")
cool.insert(1,"Kelly")
print(cool)

cool=["Evelyne", "Cole", "Jasmine"]
lucky_Numbers= [4,5,7,79,14]
print(cool)
print("\nRemove function removes an object from a list\n")
cool.remove("Cole")
print(cool)

cool=["Evelyne", "Cole", "Jasmine"]
lucky_Numbers= [4,5,7,79,14]
print(cool)
print("\nClear removes an entire list giving an empty list\n")
cool.clear()
print(cool)

cool=["\nEvelyne", "Cole", "Jasmine\n"]
print("\nPop removes the last item in the list\n")
lucky_Numbers= [4,5,7,79,14]
cool.pop()
print(cool)

cool=["Evelyne", "Cole", "Jasmine"]
lucky_Numbers= [4,5,7,79,14]
cool.index("Evelyne")
print(cool)

lucky_Numbers= [4,5,7,79,14]
print("Arranged in Ascending Order")
lucky_Numbers.sort()
print(lucky_Numbers)

lucky_Numbers= [4,5,7,79,14]
print("Display begins from the right to left/From the back to front")
lucky_Numbers.reverse()
print(lucky_Numbers)

numbers =  [5,2,4,6,8]
numbers.insert(0,20)
print(numbers)
numbers.pop()
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2.remove(5))