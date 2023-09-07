s = input()
lower, upper, numbers = [0]*26, [0]*26, [0]*10
for c in s :
    if '0' <= c <= '9' :
        numbers[ord(c) - ord('0')]+=1
    elif 'a' <= c <= 'z' :
        lower[ord(c) - ord('a')]+=1
    else :
        upper[ord(c) - ord('A')]+=1
sLower,sUpper, snumbersEven,snumbersOdd = "","","",""
for i in range(26) :
    if lower[i]!=0 :
        for _ in range(lower[i]) :
            sLower+=chr(i+ord('a'))
    if upper[i]!=0 :
        for _ in range(upper[i]) :
            sUpper+=chr(i+ord('A'))
    if i<10 and numbers[i]!=0 :
        for _ in range(numbers[i]) :
            if i%2 ==0 :
                snumbersEven+=chr(i+ord('0'))
            else :
                snumbersOdd+=chr(i+ord('0'))
print(sLower + sUpper + snumbersOdd + snumbersEven)