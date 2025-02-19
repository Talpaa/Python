def sum_above_threshold(numbers: list[int], val: int) -> int:
    
    result: int = 0

    for num in numbers:

        if num > val:

            result += num

    return result

print(sum_above_threshold([15, 5, 25], 20))#25
