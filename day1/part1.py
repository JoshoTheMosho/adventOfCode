def main():

    inputFile = 'input.txt'

    with open(inputFile) as f:
        lines = f.readlines()

    calorieTotal = 0
    maxCalorie = 0

    for l in lines:
        cal = l.replace('\n', '')
        if cal == "":
            if calorieTotal > maxCalorie:
                maxCalorie = calorieTotal
            calorieTotal = 0
        else:
            calorieTotal += int(cal)

    print(maxCalorie)

if __name__ == "__main__":
    main()