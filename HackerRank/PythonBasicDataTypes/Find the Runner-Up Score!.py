# In Space Complexity, we didn't count the arr variable, which requires space to store the input list.

###########################################
########## Time Complexity : O(1)  ########
######### Space Complexity : O(1) #########
###########################################


###########################################
########## Time Complexity : O(n)  ########
######### Space Complexity : O(1) #########
###########################################
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a,b = -102,-101
    for i in range(len(arr)) :
        if arr[i]>b :
            a = b
            b = arr[i]
        elif arr[i]<b and arr[i]>a :
            a = arr[i]
    print(a)


###########################################
##### Time Complexity : O(n * log(n)) #####
######    Space Complexity : O(n)    ######
###########################################
"""
if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    print(sorted(arr)[-2])
"""