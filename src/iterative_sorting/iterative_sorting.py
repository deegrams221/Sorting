# Resource I used: https://www.geeksforgeeks.org/selection-sort/ <-- helpful flow chart!
# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            # Selecting the smallest value
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        element1 = arr[i]
        element2 = arr[smallest_index]
        arr[i] = element2
        arr[smallest_index] = element1

        # arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = arr[i]

    return arr


# Resource I used: https://www.geeksforgeeks.org/bubble-sort/ <-- helpful visual examples
# TO-DO:  implement the Bubble Sort function below

# def bubble_sort( arr ):
#     bubbles = len(arr)

#     # iterate throught each element
#     for i in range(bubbles):
#         # last i element in place
#         for j in range(0, bubbles-i-1):
#             # iterate through array from 0 to bubbles-i-1, -1 specifies the right index
#             if arr[j] > arr[j+1]:
#                 # swap
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr

def bubble_sort( arr ):
    index = 0
    count = 0

    # while loop
    while True:
        count = 0
        for num in range(0, len(arr) - 1):
            if arr[num] > arr[num + 1]:
                #swap
                # value = arr[num]
                # arr[num] = arr[num + 1]
                # arr[num + 1] = value
                arr[num], arr[num + 1] = arr[num+1], arr[num]
                count += 1
        if count == 0:
            False
            break
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr