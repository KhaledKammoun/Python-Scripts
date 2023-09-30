from itertools import combinations_with_replacement
from math import factorial
def find_permutations_with_sum(target_sum, numbers,n):
    permutation_count = 0
    for combo in combinations_with_replacement(numbers, n):
        if sum(combo) == target_sum:
            number_of_duplicate = 1
            t = [0]*(target_sum+1)
            for x in combo :
                t[x]+=1
            
            for x in range(1,target_sum+1) :
                if t[x]!=0 :
                    number_of_duplicate*=factorial(t[x])

            permutation_count+=(factorial(n)//number_of_duplicate)
            
    return permutation_count

def reg_sum_hits(n, s):
    numbers = [x for x in range(1,s+1)]
    result = []
    for i in range(n, (n*s) + 1) :
        result.append([i,find_permutations_with_sum(i, numbers,n)])
    return result

print(reg_sum_hits(5,6))

# incomplete code
def number_of_permutation(array,n,target_sum) :
    number_of_duplicate = 1
    t = [0]*(target_sum+1)
    for x in array :
        t[x]+=1
    
    for x in range(1,target_sum+1) :
        if t[x]!=0 :
            number_of_duplicate*=factorial(t[x])

    return factorial(n)//number_of_duplicate

def make_combination(n,n_faces, s) :
    array = [1 for _ in range(n)]
    s-=(n-1)
    for i in range(n) :
        if s == 0 :
            break
        else :
            array[i] = min(s,n_faces)
            s = max(0, s-n_faces + 1)

    array = [array]
    # the rest of code

    print(array)

