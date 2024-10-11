def jump_search(array: list, value: int) -> int:
    """ Time Complexity: O(√n) """
    step = round(len(array)**(1/2))
    current = 0

    while array[current] < value:
        if current + step > len(array) - 1:
            current = len(array) - 1
            break
        else:
            current += step
    
    for i in range(current - step, current + 1):
        if array[i] == value:
            return i
    return -1

print(jump_search([2, 5, 10, 14, 20, 21], 14)) # returns 3