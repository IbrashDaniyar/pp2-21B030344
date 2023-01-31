uni_list = ['KBTU', 'SDU', 'NU']

for i, uni in enumerate(uni_list):
    print(f'{i} {uni}')



for x in "Kazakh-British Technical University":
    if x == ' ':
        break 
    if x == 't':
        continue 
    print(x)



s1 = 'python'
for i in range(len(s1)):
    print(s1[i])

for i in range(1, 11):
    print(i)
else:
    print('Finished counting to ten')


#
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
  for fruit in fruits:
    print(adj + ' ' + fruit)

for x in [0, 1, 2]:
  pass