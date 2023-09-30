def move_zeros(lst):
    count_zero = lst.count(0)
    print(count_zero)
    lst = list(filter(lambda x : x!=0, lst))
    lst+=[0]*count_zero
    return lst