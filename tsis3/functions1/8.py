def f(a):
    b=[]
    for i in a:
        if(i=="0"):
            b.append(i)
        elif (i=="7"):
            b.append(i)
    if(len(b)>=3):
        if(b[0]=="0" and b[1]=="0" and b[2]=="7"):
            print("True")
    else:
        print("False")
a=input().split()
f(a)