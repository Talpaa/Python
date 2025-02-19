def transform(num: int):

    if (num % 2) == 0:

        return int(num / 2)
    
    else:

        return int((num * 3) - 1)

print(transform(4))#2

print(transform(-10))#-5