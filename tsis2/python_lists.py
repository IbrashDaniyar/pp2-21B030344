my_list = [1, 2, 3]
print(my_list)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


list1 = ["abc", 34, True, 40, "male"]


print(type(list1))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


print(thislist[1])


print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[:4])


print(thislist[-4:-1])


if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


thislist[1] = "blackcurrant"
print(thislist)


thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist.insert(2, "watermelon")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)


print(thislist)


thislist.clear()
print(thislist)


thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


for i in range(len(thislist)):
    print(thislist[i])


i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

[print(x) for x in thislist]

my_list = [x for x in range(1, 11)]
print(my_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_upper = [x.upper() for x in fruits]
print(fruits_upper)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
num_list = [1, 3, 7, 2, 4]
num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)