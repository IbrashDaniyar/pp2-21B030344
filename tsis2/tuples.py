my_tuple = ('bmw', 'audi', 'mercedes')
print(my_tuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print(len(my_tuple), len(thistuple))

single_tuple = (1,)
not_tuple = (1)
print(single_tuple, not_tuple)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1, tuple2, tuple3)
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print(type(tuple1))

t = tuple((3, 4, 1, 7))
print(t, type(t))


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print(thistuple[-1])

print(thistuple[:2])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

thistuple = ("KBTU", "SDU", "IITU")
for x in thistuple:
  print(x)

unis = ""
for i in range(len(thistuple)):
    unis += thistuple[i] + ", "

print(unis)

i = 0
while i < len(thistuple):
  print(i, thistuple[i])
  i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)