import random
import time

import merge_sort
import quick_sort


# Generate datasets
def generate_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = sorted_data[::-1]
    random_data = random.sample(range(size * 2), size)  # unique random values
    return sorted_data, reverse_sorted_data, random_data


# Run and time sorting algorithms
def time_sort(sort_func, data):
    start_time = time.time()
    sort_func(data)
    return time.time() - start_time


# Test and compare
def compare_sorts(size):
    sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

    print(f"Data size: {size}")

    # Quick Sort timings
    print("Quick Sort Times:")
    print("  Sorted:         ", time_sort(quick_sort.quick_sort, sorted_data.copy()))
    print(
        "  Reverse Sorted: ",
        time_sort(quick_sort.quick_sort, reverse_sorted_data.copy()),
    )
    print("  Random:         ", time_sort(quick_sort.quick_sort, random_data.copy()))

    # Merge Sort timings
    print("Merge Sort Times:")
    print("  Sorted:         ", time_sort(merge_sort.merge_sort, sorted_data.copy()))
    print(
        "  Reverse Sorted: ",
        time_sort(merge_sort.merge_sort, reverse_sorted_data.copy()),
    )
    print("  Random:         ", time_sort(merge_sort.merge_sort, random_data.copy()))


# Example comparions for size 50
compare_sorts(50)

# Example comparions for size 300
compare_sorts(300)

# Example comparison for size 1000
compare_sorts(1000)
