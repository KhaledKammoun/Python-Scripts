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
