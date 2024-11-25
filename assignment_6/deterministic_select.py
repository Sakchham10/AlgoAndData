def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide the array into groups of 5
    groups = [arr[i : i + 5] for i in range(0, len(arr), 5)]

    # Find the median of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2)

    # Partition the array around the pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(left) - len(right)

    if k < len(left):
        return deterministic_select(left, k)
    elif k < len(left) + pivot_count:
        return pivot
    else:
        return deterministic_select(right, k - len(left) - pivot_count)


# Example usage:
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print(deterministic_select(arr, k - 1))  # Output: 7
