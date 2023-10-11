from math import factorial

def find_mult_3(num):
    newNum = [int(c) for c in str(num)]
    newNum.sort(reverse = True)
    result = []
    array = [0,0]
    def backtracking(newNum, subset, start, total) :
        if total % 3 == 0 and subset != [] and subset.count(0) != len(subset) :
            array[1] = max(array[1], int("".join([str(c) for c in subset.copy()])))
            t = [0]*10
            for c in subset.copy() :
                t[c]+=1
            if t[0]>0 :
                var = factorial(len(subset.copy()) - 1) * (len(subset.copy()) - t[0])
            else :
                var = factorial(len(subset.copy()))
            for i in range(10) :
                if (t[i]>0) :
                    var//=factorial(t[i])

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
    return array