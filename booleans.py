print(100 > 101)
print(0 == 0)
print('rock' in 'party rock')

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool(0))
print(bool(""))
print(bool(132))
print(bool("dsada"))
print(bool([]))
print(bool([1, 3, 1]))
print(bool(None))

isTrue = lambda: True

if isTrue:
    print("it returned true")
else:
    print("it returned false")