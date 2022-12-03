alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():

    inputFile = 'input.txt'

    with open(inputFile) as f:
        lines = f.readlines()

    total = 0

    for i in range(0, len(lines), 3):
        groupOne = list(set(lines[i].replace('\n', ''))) # Want to iterate over each set item
        groupTwo = set(lines[i+1].replace('\n', ''))
        groupThree = set(lines[i+2].replace('\n', ''))

        # Check to see which item is in the other two sets
        for letter in groupOne:

            if letter in groupTwo and letter in groupThree:
                total += getValue(letter)
                break

    print(total)

def getValue(letter):
    return alphabet.index(letter)

if __name__ == "__main__":
    main()