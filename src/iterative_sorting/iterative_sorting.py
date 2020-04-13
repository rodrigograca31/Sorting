# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for curr in range(i, len(arr)):
            if arr[curr] < arr[smallest_index]:
                smallest_index = curr

        # TO-DO: swap
        if cur_index != smallest_index:
            (arr[cur_index], arr[smallest_index]) = (
                arr[smallest_index],
                arr[cur_index],
            )
            pass

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    swaps = True
    while swaps:
        swaps = False
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                (arr[i + 1], arr[i]) = (arr[i], arr[i + 1])
                swaps = True
                pass

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


data = [7, 3, 8, 23, 7, 9, 4, 2, 8, 0, 34, 2, 7, 9, 3, 1, 9, 6, 8, -6, -9, -10]

print(len(data))
# print(selection_sort(data))
print(bubble_sort(data))
