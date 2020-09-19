NUMBERS = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
}


def cast(number: int):
    if number in NUMBERS:
        return NUMBERS[number]
    else:
        return build_roman(number)


def build_roman(number: int):
    result = ""
    while number > 0:
        r = biggest_smaller_than(NUMBERS.keys(), number)
        number -= r
        result += NUMBERS[r]
    return result


def biggest_smaller_than(NUMBERS, pivot):
    result = None
    for n in NUMBERS:
        if n > pivot:
            return result
        result = n
