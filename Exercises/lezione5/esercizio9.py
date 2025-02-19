def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    

    for i in elements_to_remove:

        while i in original_set:

            original_set.remove(i)


    return original_set


print(remove_elements({5, 6, 7}, [7, 8, 9]))