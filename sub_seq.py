def print_sub(arr, index, subarr):

    # base case
    if index == len(arr):
        print(subarr)

    else:
        # without including 
        print_sub(arr, index + 1, subarr)

        # with including
        print_sub(arr, index + 1, subarr + [arr[index]])

    return

if __name__ == '__main__':
    arr = [1, 2, 3]
    print_sub(arr, 0, [])

