import random


def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Randomly choose a pivot
    pivot = random.choice(arr)

    # Partition the array around the pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(left) - len(right)

    if k < len(left):
        return randomized_select(left, k)
    elif k < len(left) + pivot_count:
        return pivot
    else:
        return randomized_select(right, k - len(left) - pivot_count)
