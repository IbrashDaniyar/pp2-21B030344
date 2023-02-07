import itertools
def f(s):
    s1=itertools.permutations(s)
    for i in s1:
     i = "".join(i)
     print(i)
s=input()
f(s)