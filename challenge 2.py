from collections import deque

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Asegura que no se hagan rotaciones de más
    queue = deque(arr)
    for _ in range(k):
        queue.appendleft(queue.pop())
    return list(queue)
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # [5, 6, 7, 1, 2, 3, 4]
print(rotate_array([10, 20, 30, 40], 1))      # [40, 10, 20, 30]
print(rotate_array([1, 2], 5))                # [2, 1]
