# python3
# Edgars Lejnieks, 7. grupa


def build_heap(data):
    swaps = []
    # TODO: Create heap (min) and heap sort
    # try to achieve  O(n) and not O(n2)

    print("stuff is happening")

    data_len = len(data)
    #print(data_len)
    if data_len % 2 == 0:
        iter_len = int(data_len/2-2)
    else:
        iter_len = int(data_len/2-1)
    # print(iter_len)
    min_val  = 0
    check    = True
    counter  = 0

    # debug_swapcounter = 0

    while(True):
        check = False
        counter += 1

        for iter in range (iter_len, -1, -1):
            # if iter < 10:
            #     print(iter)
            #print(iter)

            min_val = min(data[iter], data[2*iter+1], data[2*iter+2])

            if min_val == data[2*iter+1]:
                data[iter], data[2*iter+1] = data[2*iter+1], data[iter]
                swaps.append([iter, 2*iter+1])
                debug_swapcounter += 1
                # print(debug_swapcounter)
                check = True
                

            elif min_val == data[2*iter+2]:
                data[iter], data[2*iter+2] = data[2*iter+2], data[iter]
                swaps.append([iter, 2*iter+2])
                debug_swapcounter += 1
                # print(debug_swapcounter)
                check = True

        if counter == iter_len:
            if check == False:
                # print("break")
                break
            else:
                counter = 0

    # this do NOT sort the heap... i guess
    # 2*i+1 - kreisā puse
    # 2*i+2 - labā puse

    
    # for i in range(data_len):
    #     if 2*i+1 <= data_len-1:
    #         # 𝑎𝑖 < 𝑎2𝑖+1.
    #         if data[i] >= data[2*i+1]:
    #             data[i], data[2*i+1] = data[2*i+1], data[i]
    #             swaps.append([i, 2*i+1])
    #     if 2*i+2 <= data_len-1:
    #         if data[i] >= data[2*i+2]:
    #                 data[i], data[2*i+2] = data[2*i+2], data[i]
    #                 swaps.append([i, 2*i+2])
        
    #implementation: O(n10)


    # pos_of_max = 0
    # for n, m in enumerate(data):
    #     if m > pos_of_max:
    #         pos_of_max = n

    # check = False
    # while check != True:

    #     for i, j in enumerate(data):
    #         if pos_of_max == data_len-1:
    #             check = True
    #         kreisapuse = 2*i+1
    #         labapuse = 2*i+2
    #         if kreisapuse >= data_len:
    #             break
    #         if labapuse >= data_len:
    #             break
    #         print(i)
    #         if kreisapuse >= labapuse and data[kreisapuse] < data[pos_of_max]:
    #             data[i], data[kreisapuse] = data[kreisapuse], data[i]
    #             check = False
    #             swaps.append([i, kreisapuse])

    #         if labapuse >= kreisapuse and data[labapuse] < data[pos_of_max]:
    #             data[i], data[labapuse] = data[labapuse], data[i]
    #             check = False
    #             swaps.append([i, labapuse])


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
            #github is looking for file 04
            filepath = "tests/" + filepath
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
