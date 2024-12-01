def main():

    list_1 = []
    list_2 = []

    with open("input.txt", "r") as f:
        for line in f:
            split = line.split()
            list_1.append(int(split[0]))
            list_2.append(int(split[1]))

    list_1.sort()
    list_2.sort()
    
    total = 0
    for i in range(len(list_1)):
        total += abs(list_1[i] - list_2[i])
        

    print(total)


if __name__ == "__main__":
    main()
