alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():

    inputFile = 'input.txt'

    with open(inputFile) as f:
        lines = f.readlines()

    total = 0

    for l in lines:
        halfLen = int(len(l) / 2)
        packOne = l[:halfLen] # Build our first rucksack
        packTwo = l[halfLen:] # Build our second rucksack

        currItems = set() # Build a set with every 'item' or char

        for i in packOne:
            currItems.add(i)

        for j in packTwo:
            if j in currItems: # Once we find j in the set, we know we have a match
                total += getValue(j)
                break

    print(total)

def getValue(letter):
    return alphabet.index(letter)

if __name__ == "__main__":
    main()