def long_subseq(integers : str) -> list:
    i_list = integers.split()
    if not i_list:
        return None

    integer_list = [int(i) for i in i_list]
    max_len = 1
    result = [integer_list[0]]
    ptr1 = 0
    ptr2 = 1
    while ptr2 < len(integer_list):
        if integer_list[ptr2] <= integer_list[ptr2 - 1]:
            # decreasing
            # update result and max length if a longer subsequence is found
            length = ptr2 - ptr1
            if length > max_len:
                max_len = length
                result = integer_list[ptr1:ptr2]

            # reset the starting pointer
            ptr1 = ptr2

        ptr2 += 1

    # update result if a longer subsequence is found at the end of the list
    if ptr2 - ptr1 > max_len:
        result = integer_list[ptr1:ptr2]

    return result

if __name__ == "__main__":
    while True:
        integers = input("Enter a list of integers(enter or type exit to exit): ")
        if not integers or integers.lower() == 'exit':
            break

        print (long_subseq(integers))
