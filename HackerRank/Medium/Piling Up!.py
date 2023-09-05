T = int(input())
for _ in range(T) :
    n = int(input())
    blocks = list(map(int, input().split()))
    i,j = 0, n-1
    maximum = 2147483648
    test = True
    while (i<j) :
        maximum_var = 0
        if blocks[i] >= blocks[j] :
            maximum_var = blocks[i]
            i+=1
        else :
            maximum_var = blocks[j]
            j-=1
        if (maximum_var > maximum) :
            test = False
            break
        else :
            maximum = maximum_var
    if test :
        print("Yes")
    else :
        print("No")