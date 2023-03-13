"""
python3
Edgars Lejnieks, 7. grupa
"""


def build_heap(data):
    swaps = []
    # TODO: Create heap (min) and heap sort
    # try to achieve  O(n) and not O(n2)

    data_len = len(data)
    #min_val = min(data)
    #min_val_index = data.index(min_val)
    #data[0], data[min_val_index] = data[min_val_index], data[0]
    #swaps.append([0, min_val_index]) #O(1)

    for i in range(data_len):
        if 2*i+1 <= data_len-1:
            # 𝑎𝑖 < 𝑎2𝑖+1.
            if data[i] >= data[2*i+1]:
                data[i], data[2*i+1] = data[2*i+1], data[i]
                swaps.append([i, 2*i+1])
        if 2*i+2 <= data_len-1:
            if data[i] >= data[2*i+2]:
                    data[i], data[2*i+2] = data[2*i+2], data[i]
                    swaps.append([i, 2*i+2])
        
    #current implementation: O(n10)
    #i dont even know if it works
    #:D


    return swaps


def main():

    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file

    inputtype = input()

    # previous implementation of input type check
    if "I" in inputtype:
        try:
            # print("Input node count: ")
            n = int(input())
            # print("Input node values: ")
            data = list(map(int, input().split()))

        except EOFError as e:
            print(e)
        

    elif "F" in inputtype:
        try:
            # print("Input file path ")
            filepath = input()
            file = open(filepath, "r")
            #data = list(map(int, file.readlines().split()))
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
            file.close()
        except EOFError as e:
            print(e) 


    # input from keyboard
    # n = int(input())
    # data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
