if __name__ == '__main__':
    N = int(input())
    liste = []
    for _ in range(N) :
        liste_1 = input().split()
        s, numbers = liste_1[0], list(map(int, liste_1[1:]))
        if (s == "insert") :
            liste.insert(numbers[0], numbers[1])
        elif s == "print" :
            print(liste)
        elif s == "remove" :
            liste.remove(numbers[0])
        elif s == "append" :
            liste.append(numbers[0])
        elif s == "sort" :
            liste.sort()
        elif s == "pop" :
            liste.pop()
        else :
            liste.reverse()