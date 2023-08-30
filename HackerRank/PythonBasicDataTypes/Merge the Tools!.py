def merge_the_tools(string, k):
    n,var = len(string), 0
    for i in range (0,n//k) :
        x = ""
        for c in string[var:k+var] :
            if not c in x :
                x+=c
        print(x)
        var+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)