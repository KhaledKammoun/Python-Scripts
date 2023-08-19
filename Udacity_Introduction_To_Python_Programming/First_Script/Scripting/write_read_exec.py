with open('new_file.py','w') as f :
    f.write('''\
for i in range(10) :
    if (i%2==0) :
        print("Odd  : {}".format(i))
    else :
        print("Even : {}".format(i))   
''')
with open('new_file.py', 'r') as f:
    code_to_execute = f.read()
exec(code_to_execute)

"""
REMARQUE :
with open('all_lines.txt','w') as f:
    f.write("Hello World!!!\nABC!!!")
with open('all_lines.txt','r') as f :
    x = f.readlines() 
print(x) # ["Hello World!!!\n", "ABC!!!"]
"""