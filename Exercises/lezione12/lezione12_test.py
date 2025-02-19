'''i: int = 0
test_value: int = 0

assert i == 0, f'Error, the variable i must be {test_value} instead is {i}'''

#python -m unittest -v

def sum(a: int, b: int)-> int:

    return 0

result: int = sum(a=5, b=2)

test_value: int = 7
assert result == test_value, f'Error, the variable i must be {test_value} instead is {result}'

result: int = sum(a=4, b=2)

test_value: int = 6
assert result == test_value, f'Error, the variable i must be {test_value} instead is {result}'
