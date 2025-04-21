def sliding_window_maximum(nums, k):
    if not nums:
        return []

    deque = []  
    result = []

    for i in range(len(nums)):
        if deque and deque[0] < i - k + 1:
            deque.pop(0)  

        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()

        deque.append(i)

        if i >= k - 1:
            result.append(nums[deque[0]])

    return result


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
print(sliding_window_maximum([9, 11], 2))                      # [11]
print(sliding_window_maximum([4, 2, 12, 3, 8], 1))             # [4, 2, 12, 3, 8]
