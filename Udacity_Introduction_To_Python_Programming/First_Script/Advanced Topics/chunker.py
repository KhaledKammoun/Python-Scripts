def chunker(iterable, size) :
    for i in range(iterable[0],iterable[-1] + 1,size) :
        yield iterable[i:i+size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

##### Generators and list comprehension
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares