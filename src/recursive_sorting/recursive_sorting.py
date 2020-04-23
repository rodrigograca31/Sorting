# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # TO-DO
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if(arrA[i] < arrB[j]):
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    # i = 0
    # j = 0
    # for ele in range(0, elements):
    #     if len(arrA) <= i:
    #         merged_arr[ele] = arrB[j]
    #         j += 1
    #     elif len(arrB) <= j:
    #         merged_arr[ele] = arrA[i]
    #         i += 1
    #     elif arrA[i] < arrB[j]:
    #         merged_arr[ele] = arrA[i]
    #         i += 1
    #     else:
    #         merged_arr[ele] = arrB[j]
    #         j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # TO-DO
    if(len(arr) > 1):
        middle = len(arr)//2
        # print(middle)
        LHS = (arr[:middle])
        RHS = (arr[middle:])

        return merge(merge_sort(LHS), merge_sort(RHS))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


# print(merge([1, 2, 3], [4, 5, 6]))
print(merge_sort([9, 3, 5,  5, 4, 2]))
