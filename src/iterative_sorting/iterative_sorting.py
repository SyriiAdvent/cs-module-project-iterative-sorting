from raw_input_list import lst


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # Swap Code
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

selection_sort([5,2,1,7,8,9,32])
# selection_sort(lst)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr):
        maximum = arr[0]
    else:
        return []

    for i in arr:
        if i > maximum:
            maximum = i
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
    count = [0] * (maximum + 1)

    for i in arr:
        count[i] += 1

    new_arr = []
    for value, count in enumerate(count):
        for i in range(count):
            new_arr.append(value)

    return new_arr