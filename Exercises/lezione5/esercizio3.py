def find_element(lst: list[int], element: int) -> bool:
    for item in lst:

        if item == element:
            return True
        
    return False


print(find_element([1, 2, 3, 4, 5], 5))