def create_flowerdict(filename):
    flowerdict = dict()
    with open(filename) as f :
        for line in f :
            letterFlower = line.split(": ")
            letter,flowerName = letterFlower[0].lower(),letterFlower[1].strip()
            flowerdict[letter] = flowerName
    return flowerdict

def main() :
    flowerdict = create_flowerdict("flowers.txt")
    userName = input("Enter your First [space] Last name only: ")
    firstUserLetter = userName[0].lower()
    print("Unique flower name with the first letter: {}".format(flowerdict[firstUserLetter]))
main()