import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


for x in range(5):
    random_size = random.randint(1, 10)
    arr = []
    for x in range(random_size):
        arr.append(random.randint(-10, 1000))
    print("Before sorting")
    print(arr)
    insertion_sort(arr)
    print("After sorting")
    print(arr)
