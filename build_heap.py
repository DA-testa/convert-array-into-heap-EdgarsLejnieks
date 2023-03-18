# python3
# Edgars Lejnieks, 7. grupa


def build_heap(data):
    swaps = []
    # TODO: Create heap (min) and heap sort
    # try to achieve  O(n) and not O(n2)

    #print("stuff is happening")

    data_len = len(data)
    #print(data_len)
    if data_len % 2 == 0:
        iter_len = data_len//2-2 #only just now found out about floor division
    else:
        iter_len = data_len//2-1
    # print(iter_len)
    min_val  = 0
    check    = True
    counter  = 0

    debug_swapcounter = 0

    #apparently this loop never finishes, and i sure do wonder why :D
    #timeout at 300'000 miliseconds
    while(check == True):
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
        
        if debug_swapcounter % 1000 == 0:
            print(debug_swapcounter)

        if counter == iter_len:
            if check == False:
                # print("break")
                break
            else:
                counter = 0
    
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
    #does not work

    return swaps


def main():

    inputtype = input()

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
