n = int(input())
m = dict()

for _ in range(n) :
    string = input()
    m[string] = m.get(string,0)+1

print(len(m))

for key in m :
    print(m[key],end=" ")

    