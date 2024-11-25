import random
import time

from deterministic_select import deterministic_select
from randomized_select import randomized_select


def test_selection_algorithms():
    sizes = [10, 50, 100, 1000, 5000, 10000]
    results = []

    for size in sizes:
        # Generate a random array of the given size
        arr = [random.randint(0, 1000000) for _ in range(size)]
        k = random.randint(0, size - 1)  # Random k within the array size

        print(f"Testing array of size {size} with k = {k}...")

        # Test Deterministic Select
        start_time = time.time()
        result_deterministic = deterministic_select(arr[:], k)  # Use a copy of arr
        deterministic_time = time.time() - start_time
        print(
            f"  Deterministic Select: {result_deterministic}, Time: {deterministic_time:.6f} seconds"
        )

        # Test Randomized Select
        start_time = time.time()
        result_randomized = randomized_select(arr[:], k)  # Use a copy of arr
        randomized_time = time.time() - start_time
        print(
            f"  Randomized Select: {result_randomized}, Time: {randomized_time:.6f} seconds"
        )

        # Store results
        results.append(
            {
                "size": size,
                "k": k,
                "deterministic_time": deterministic_time,
                "randomized_time": randomized_time,
                "result_deterministic": result_deterministic,
                "result_randomized": result_randomized,
            }
        )

        # Validate that both algorithms produce the same result
        assert (
            result_deterministic == result_randomized
        ), f"Mismatch: Deterministic={result_deterministic}, Randomized={result_randomized}"

    # Summary of results
    print("\nSummary:")
    for result in results:
        print(f"Array Size: {result['size']}, k: {result['k']}")
        print(f"  Deterministic Time: {result['deterministic_time']:.6f} seconds")
        print(f"  Randomized Time: {result['randomized_time']:.6f} seconds")


if __name__ == "__main__":
    test_selection_algorithms()
