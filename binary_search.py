def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target value.

    Args:
        arr (list): The sorted array to search in.
        target: The value to search for.

    Returns:
        tuple: A tuple containing the number of iterations performed and the best match found.
               If the target value is found, the best match will be the target value itself.
               If the target value is not found, the best match will be the closest value to the target.

    """
    left, right = 0, len(arr) - 1
    iterations = 0
    best_match = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            best_match = arr[mid]
            left = mid + 1
        else:
            right = mid - 1

    if best_match is not None and best_match >= target:
        return (iterations, best_match)
    else:
        return (iterations, arr[left] if left < len(arr) else arr[right])


# Приклад використання:
sorted_array = [0.1, 0.5, 0.9, 1.2, 1.5, 2.3, 3.6]
result = binary_search(sorted_array, 1.4)
print(result)  # Output: (кількість ітерацій, верхня межа)
