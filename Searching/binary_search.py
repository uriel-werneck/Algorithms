def binary_search(array: list, value: int) -> bool:
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return True
        elif array[mid] > value:
            right = mid - 1
        elif array[mid] < value:
            left = mid + 1
    
    return False