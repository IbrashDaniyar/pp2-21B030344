def un(a):
    b = []
    for i in a:
         if i not in b:
            b.append(i)
    b = " ".join(b)
    print(b)
a = input().split()
un(a)