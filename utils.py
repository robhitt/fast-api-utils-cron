total = 0
num = 2


def multiply_by_two():
    global total
    if total != 0:
        total = total + (num * 2)
    else:
        total = num

    return total
