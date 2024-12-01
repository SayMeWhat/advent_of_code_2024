def main():

    my_map = {}
    list_1 = []
    list_2 = []

    with open("input.txt", "r") as f:
        for line in f:
            split = line.split()
            list_1.append(int(split[0]))
            list_2.append(int(split[1]))

    
    for val in list_1:
        if val not in my_map:
            my_map[val] = 0

    for val in list_2:
        if val in my_map:
            my_map[val] += 1

    total = 0 
    for val in list_1:
        total += my_map[val] * val
        

if __name__ == "__main__":
    main()
