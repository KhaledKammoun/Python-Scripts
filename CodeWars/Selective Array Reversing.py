def sel_reverse(arr,l):
    if (l>0) :
        for i in range(0, len(arr), l) :
            arr[i:i+l] = arr[i:i+l][::-1]
    return arr

"""
def sel_reverse(arr,l):
    return [x for i in range(0, len(arr), l) for x in arr[i:i+l][::-1]] if (l!=0) else arr
"""