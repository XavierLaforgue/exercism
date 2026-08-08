def steps(number):
    if number < 1 or not isinstance(number, int):
        raise ValueError('Only positive integers are allowed')
    step = 0
    while number > 1:
        step += 1
        isEven = number % 2 == 0
        if isEven:
            number /= 2
        else:
            number = number * 3 + 1
    return step
