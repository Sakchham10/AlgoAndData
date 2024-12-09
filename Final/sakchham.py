import time

import numpy as np


# Naive Implementation
def naive_matmul(A, B):
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C


# Optimized Implementation
def optimized_matmul(A, B):
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C


# Performance Test
n = 500
A = np.random.rand(n, n)
B = np.random.rand(n, n)

start_time = time.time()
naive_matmul(A, B)
naive_time = time.time() - start_time

start_time = time.time()
optimized_matmul(A, B)
optimized_time = time.time() - start_time

print(f"Naive Time: {naive_time:.2f} seconds")
print(f"Optimized Time: {optimized_time:.2f} seconds")
