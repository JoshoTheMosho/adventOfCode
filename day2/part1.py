def main():

    inputFile = 'input.txt'

    with open(inputFile) as f:
        lines = f.readlines()

    score = 0
    
    # A rock, B paper, C scissors
    # X lose, Y draw, Z scissors
    # 1 rock, 2 paper, 3 scissors
    scoreMap = {
        'AX': 3 + 1,
        'AY': 6 + 2,
        'AZ': 0 + 3,
        'BX': 0 + 1,
        'BY': 3 + 2,
        'BZ': 6 + 3,
        'CX': 6 + 1,
        'CY': 0 + 2,
        'CZ': 3 + 3
    }

    for l in lines:
        score += scoreMap[l[0] + l[2]]

    print(score)

if __name__ == "__main__":
    main()