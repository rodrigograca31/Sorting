import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        previous = i - 1

        while previous >= 0 and current < arr[previous]:
            arr[previous+1] = arr[previous]
            previous -= 1
        arr[previous+1] = current
    return arr


# first pseudocode: https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort2(arr):
    for i in range(1, len(arr)):

        j = i
        while j > 0 and arr[j-1] > arr[j]:
            (arr[j], arr[j-1]) = (arr[j-1], arr[j])
            j -= 1
    return arr

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        if cur_index != smallest_index:
            (arr[cur_index], arr[smallest_index]) = (
                arr[smallest_index],
                arr[cur_index],
            )
            pass

    return arr


def selection_sort2(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

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


data = [3, 2, 7, 2, 9, 1]
print(insertion_sort(data))

# times = 1000


# start = time.time()
# for x in range(times):
#     (selection_sort(data))
# print("Imp 1: \t%.8f" % float(time.time() - start))

# start = time.time()
# for x in range(times):
#     (selection_sort2(data))
# print("Imp 2: \t%.8f" % float(time.time() - start))

# start = time.time()
# for x in range(times):
#     (insertion_sort(data))
# print("Imp 3: \t%.8f" % float(time.time() - start))
