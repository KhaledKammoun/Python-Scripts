def merge_the_tools(string, k): # Time Complextity : O(n)
    n,var = len(string), 0
    for _ in range (n//k) : # O(n//k)
        x = ""
        for c in string[var:k+var] : # O(k)
            if not c in x :
                x+=c
        print(x)
        var+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)