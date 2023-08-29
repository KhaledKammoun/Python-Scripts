def chunker(iterable, size) :
    for i in range(iterable[0],iterable[-1] + 1,size) :
        yield iterable[i:i+size]

for chunk in chunker(range(25), 4):
    print(list(chunk))