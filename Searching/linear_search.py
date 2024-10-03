def linear_search(array: list, value: int) -> int:
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1