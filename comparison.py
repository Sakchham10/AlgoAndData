import os
import random
import sys
import time
import tracemalloc

sys.path.append(
    os.path.abspath("/Users/sakchhamsangroula/Projects/AlgoAndData/assignment_4")
)

sys.path.append(
    os.path.abspath("/Users/sakchhamsangroula/Projects/AlgoAndData/assignment_2")
)

from heapsort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def performance_test(sort_func, arr):
    tracemalloc.start()
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak


def generate_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = sorted_data[::-1]
    random_data = random.sample(range(size * 2), size)
    return sorted_data, reverse_sorted_data, random_data


def quick_sort_wrapper(arr):
    quick_sort(arr, 0, len(arr) - 1)


def compare_sorts(size):
    sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

    # Run performance tests
    print(f"Testing Quick Sort on dataset of {size} numbers")
    quick_sorted_time, quick_sorted_memory = performance_test(
        quick_sort_wrapper, sorted_data.copy()
    )
    quick_reverse_sorted_time, quick_reverse_sorted_memory = performance_test(
        quick_sort_wrapper, reverse_sorted_data.copy()
    )
    quick_random_time, quick_random_memory = performance_test(
        quick_sort_wrapper, random_data.copy()
    )

    merge_sorted_time, merge_sorted_memory = performance_test(
        merge_sort, sorted_data.copy()
    )
    merge_reverse_sorted_time, merge_reverse_sorted_memory = performance_test(
        merge_sort, reverse_sorted_data.copy()
    )
    merge_random_time, merge_random_memory = performance_test(
        merge_sort, random_data.copy()
    )

    heap_sorted_time, heap_sorted_memory = performance_test(
        heap_sort, sorted_data.copy()
    )
    heap_reverse_sorted_time, heap_reverse_sorted_memory = performance_test(
        heap_sort, reverse_sorted_data.copy()
    )
    heap_random_time, heap_random_memory = performance_test(
        heap_sort, random_data.copy()
    )

    # Display results
    print(
        f"Quick Sort - Sorted Data: {quick_sorted_time:.6f} sec, {quick_sorted_memory} bytes"
    )
    print(
        f"Quick Sort - Reverse Sorted Data: {quick_reverse_sorted_time:.6f} sec, {quick_reverse_sorted_memory} bytes"
    )
    print(
        f"Quick Sort - Random Data: {quick_random_time:.6f} sec, {quick_random_memory} bytes\n"
    )

    print(f"Testing Merge Sort on dataset of {size} numbers")

    print(
        f"Merge Sort - Sorted Data: {merge_sorted_time:.6f} sec, {merge_sorted_memory} bytes"
    )
    print(
        f"Merge Sort - Reverse Sorted Data: {merge_reverse_sorted_time:.6f} sec, {merge_reverse_sorted_memory} bytes"
    )
    print(
        f"Merge Sort - Random Data: {merge_random_time:.6f} sec, {merge_random_memory} bytes"
    )

    print()

    print(f"Testing Heap Sort on dataset of {size} numbers")

    print(
        f"Heap Sort - Sorted Data: {heap_sorted_time:.6f} sec, {heap_sorted_memory} bytes"
    )
    print(
        f"Heap Sort - Reverse Sorted Data: {heap_reverse_sorted_time:.6f} sec, {heap_reverse_sorted_memory} bytes"
    )
    print(
        f"Heap Sort - Random Data: {heap_random_time:.6f} sec, {heap_random_memory} bytes"
    )
    print()


compare_sorts(10)
compare_sorts(100)
compare_sorts(1000)
compare_sorts(2000)
