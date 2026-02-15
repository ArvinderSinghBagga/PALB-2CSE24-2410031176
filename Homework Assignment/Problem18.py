def is_subset(a, b):
    count = {}

    for num in a:
        count[num] = count.get(num, 0) + 1

    for num in b:
        if count.get(num, 0) == 0:
            return False
        count[num] -= 1

    return True
