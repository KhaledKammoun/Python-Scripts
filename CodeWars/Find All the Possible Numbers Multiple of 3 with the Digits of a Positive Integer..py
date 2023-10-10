from math import factorial

def find_mult_3(num):
    newNum = [int(c) for c in str(num)]
    newNum.sort(reverse = True)
    result = []
    array = [0,0]
    def backtracking(newNum, subset, start, total) :
        if total % 3 == 0 and subset != [] and subset !=[0] :
            array[1] = max(array[1], int("".join([str(c) for c in subset.copy()])))
            t = [0]*9
            for c in subset.copy() :
                t[c]+=1
            var = factorial(len(subset.copy()))
            for i in range(1,9) :
                if (t[i]>0) :
                    var//=factorial(t[i])
            if (t[0]>0) :
                var-=(factorial(len(subset.copy()))//(factorial(len(subset.copy()) - t[0])))
            array[0]+=var
            result.append(subset.copy())
        elif start >= len(newNum) :
            return
        
    
        i = start
        while i < len(newNum) :
            
            subset.append(newNum[i])
            backtracking(newNum, subset, i + 1, total + newNum[i])
            subset.pop()
            while i + 1 < len(newNum) and newNum[i] == newNum[i + 1] :
                i += 1
            i += 1
    backtracking(newNum, [], 0, 0)
    print(result)
    print(array)

find_mult_3(6063)
