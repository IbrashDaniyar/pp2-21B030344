x1 = 1
x2 = 3.6
x3 = 1 + 1j
my_list = [x1, x2, x3]

my_list_types = [type(x) for x in my_list]

for x in my_list:
    print(f'{x} of type {type(x)}')