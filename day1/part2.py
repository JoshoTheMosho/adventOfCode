def main():

    inputFile = 'input.txt'

    with open(inputFile) as f:
        lines = f.readlines()

    calorieTotal = 0
    maxCalorie1 = 0
    maxCalorie2 = 0
    maxCalorie3 = 0

    for l in lines:
        cal = l.replace('\n', '')
        if cal == "":
            if calorieTotal > maxCalorie1:
                maxCalorie1 = calorieTotal
            elif calorieTotal > maxCalorie2:
                maxCalorie2 = calorieTotal
            elif calorieTotal > maxCalorie3:
                maxCalorie3 = calorieTotal
            calorieTotal = 0
        else:
            calorieTotal += int(cal)

    print(maxCalorie1 + maxCalorie2 + maxCalorie3)

if __name__ == "__main__":
    main()