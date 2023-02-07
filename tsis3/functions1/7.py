def has_33():
    a=input().split()
    cnt=0
    for i in range(len(a)-1):
        if(a[i]=="3" and a[i+1]=="3"):
            cnt+=1           
    if (cnt=="0"):
        print("False")
    else:
         print("True")

has_33()