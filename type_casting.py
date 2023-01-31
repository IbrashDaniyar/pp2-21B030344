x1 = int(2)
x2 = int(3.5)
x3 = int("3")

my_list = [x1, x2, x3]

y1 = float(6)
y2 = float(2.1)
y3 = float("4.4")
my_list.extend([y1, y2, y3])

s1 = str(2)
s2 = str(1.5)
s3 = str("Hello")
my_list.extend([s1, s2, s3])

for x in my_list:
    print(f'{x} of type {type(x)}')