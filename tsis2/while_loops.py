my_list = [x for x in range(10)]
i = 0
while i < len(my_list):
    if i == 0:
        continue
    if i > 5:
        break 
    print(my_list[i])
    i += 1