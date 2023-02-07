def solve(numheads,numlegs):
    for a in range (numheads):
        for b in range (numlegs):
            if(a+b==numheads and 2*a+4*b==numlegs):
                print(a,b)
solve(35,94)