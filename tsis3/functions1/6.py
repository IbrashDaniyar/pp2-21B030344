def f(a):
    b = a[::-1]
    c = " ".join(b)
    print(c)

a = input().split()
f(a)