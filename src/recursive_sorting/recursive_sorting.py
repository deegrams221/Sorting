# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        # of the length of arrA == 0, and merged_arr[i] is arrB[0], then remove and return the first num in arrB
        if (len(arrA) == 0):
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        # else if the len of arrB == 0, and merged_arr[i] is arrA[0], then remove and return the first num in arrA
        elif (len(arrB) == 0):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        # else if the arrA[0] is less than or equal to arrB[0], and merged_arr[i] is arrA[0], then remove and return the first num in arrA
        elif (arrA[0] <= arrB[0]):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        # else, merged_arr[i] is arrB[0], then remove and return the first num in arrB
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if len(arr) is greater than 1
    if len(arr) > 1:
    # find middle of array brake in half
        left = arr[:len(arr) // 2]
        right = arr[len(arr) // 2:]

        # sort the 2 halfs
        left = merge_sort(left)
        right = merge_sort(right)

        # merges left, right
        arr = merge(left, right)

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
def timsort( arr ):

    return arr
