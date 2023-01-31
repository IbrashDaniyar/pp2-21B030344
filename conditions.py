inp_num = int(input("Enter the number"))
if inp_num > 0:
    print("Number is greater than 0")
elif inp_num < 0: 
    print("Number is less than 0")
else:
    print("Number is 0")

if inp_num > 0:
    pass
else:
    print("You shall not pass")

a = 4
b = 3
if a > b: print("a is greater than b")

print("A") if a > b else print("B")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

c = 330
if a == b and b == c:
    print("three numbers are true")

b = 0
if a > b or a > c:
    print("a is greater than b or c")

c = 3
if a > b:
    if a > c:
        print("of 3 a is the greatest num")