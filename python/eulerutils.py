
def int2base(x, base):
    if base < 2:
        raise ValueError("base must be greater or equals to 2")
    if base > 16:
        raise ValueError("base must be less or equals to 16")
    hexdigits = "0123456789ABCDEF"
    if x == 0:
        return 0
    elif x < 0:
        sign = -1
        x = -x
    else:
        sign = 1
    result = ""
    while x:
        result += hexdigits[x % base]
        x = x // base
    if sign < 0:
        return "-" + result[::-1]
    return result[::-1]
