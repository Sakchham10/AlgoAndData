import random
import time
import tracemalloc

from merge_sort import merge_sort
from quick_sort import quick_sort


# Generate datasets
def generate_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = sorted_data[::-1]
    random_data = random.sample(range(size * 2), size)  # unique random values
    return sorted_data, reverse_sorted_data, random_data


# Run and time sorting algorithms
def measure_time_memory(sort_func, data):
    tracemalloc.start()  # Start memory tracking
    start_time = time.time()
    sort_func(data)
    duration = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop memory tracking
    return duration, peak


# Test and compare
def compare_sorts(size):
    sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

    print(f"Data size: {size}")

    # Quick Sort timings and memory
    print("Quick Sort Times and Memory Usage:")
    for name, data in [
        ("Sorted", sorted_data),
        ("Reverse Sorted", reverse_sorted_data),
        ("Random", random_data),
    ]:
        time_taken, memory_used = measure_time_memory(quick_sort, data.copy())
        print(
            f"  {name}: Time = {time_taken:.6f} sec, Peak Memory = {memory_used / 1024:.2f} KB"
        )

    # Merge Sort timings and memory
    print("\nMerge Sort Times and Memory Usage:")
    for name, data in [
        ("Sorted", sorted_data),
        ("Reverse Sorted", reverse_sorted_data),
        ("Random", random_data),
    ]:
        time_taken, memory_used = measure_time_memory(merge_sort, data.copy())
        print(
            f"  {name}: Time = {time_taken:.6f} sec, Peak Memory = {memory_used / 1024:.2f} KB"
        )


# Example comparions for size 5000
compare_sorts(5000)

# Example comparions for size 30000
compare_sorts(30000)

# Example comparison for size 100000
compare_sorts(100000)

# Example comparison for size 200000
compare_sorts(200000)
