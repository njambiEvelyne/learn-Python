alien_0= {
    "color":"green",
    "points":5,

}
print(dir(alien_0))
#print(help(alien_0))

print(alien_0.get("color"))
nos = list(range(1,11))
print(nos)
num =  nos[::-1]
print(num)

def square(digit):
    return digit * digit

digit = int(input("Enter the number: "))
squares = square(digit)
print(squares)

a = {1,2,3,4,5,6,7,8,9,10}
b= {1,2,3,6,9,10}
c = b.intersection(a)
print(c)
d = a .union(b)
print(d)
e = a .difference(b)
print(e)
f = b.difference(a)
print(f)
g = 3
print(g in a)
