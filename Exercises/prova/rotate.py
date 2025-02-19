def rotate_element(elements: list, k: int)->list:
    
    k = k % (len(elements))

    print(k)

    for i in range(k):
    
        element: int = elements.pop((len(elements))-1)
        elements.insert(0, element)

    return elements


print(rotate_element([1, 2, 3, 4, 5], 2))

print(rotate_element([1, 2, 3, 4, 5], 8))