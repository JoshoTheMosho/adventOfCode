def main():

    inputFile = 'input.txt'

    with open(inputFile) as f:
        lines = f.readlines()

    score = 0
    
    # A rock, B paper, C scissors
    # X lose, Y draw, Z win
    # 1 rock, 2 paper, 3 scissors
    scoreMap = {
        'AX': 0 + 3, # rock beats scissors
        'AY': 3 + 1, # rock draws rock
        'AZ': 6 + 2, # rock loses paper
        'BX': 0 + 1, # paper beats rock
        'BY': 3 + 2, # paper ties paper
        'BZ': 6 + 3, # paper loses scissors
        'CX': 0 + 2, # scissors beats paper
        'CY': 3 + 3, # scissors ties scissors
        'CZ': 6 + 1 # scissors beats scissors
    }

    for l in lines:
        score += scoreMap[l[0] + l[2]]

    print(score)

if __name__ == "__main__":
    main()