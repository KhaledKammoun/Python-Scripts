"""
INPUT: string, A single line of input consisting of the string .

OUTPUT:string, A single line of output consisting of the modified string.

EXAMPLE : 
    ** Sample Input
        1222311

    ** Sample Output
        (1, 1) (3, 2) (1, 3) (2, 1)
"""
s = input()
output = ""
x,char = 0,s[0]
for c in s+" " :
    if c==char :
        x+=1
    else :
        output+="({}, {}) ".format(str(x),char)
        x = 1
        char = c
print(output[:-1])
        