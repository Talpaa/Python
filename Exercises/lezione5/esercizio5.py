def rounded_average(numbers: list[int]) -> int:
    
    media: int = 0

    for i in numbers:

        media += i

    media = media/len(numbers)

    if (media % 1) >= 0.5:

        media = (media//1)+1

    elif (media % 1) < 0.5:

        media = media//1

    return media



print(rounded_average([1, 1, 2, 2])) #output 2