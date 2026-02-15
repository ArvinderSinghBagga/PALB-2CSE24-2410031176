def factorial(n):
    res = [1]

    for x in range(2, n + 1):
        carry = 0
        for i in range(len(res)):
            val = res[i] * x + carry
            res[i] = val % 10
            carry = val // 10

        while carry:
            res.append(carry % 10)
            carry //= 10

    return res[::-1]
