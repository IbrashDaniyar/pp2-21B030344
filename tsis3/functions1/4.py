def f(a):
      for i in range(len(a)):
            a[i]=int(a[i])
            ans=True
            if(a[i]==1 or a[i]==2):
                  ans=False
            for k in range(2,a[i]):
                  if(a[i]%k==0):
                        ans=False
                        break
            if (ans==True):
                 print(a[i])

a=input().split()
f(a)