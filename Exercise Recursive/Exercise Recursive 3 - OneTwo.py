def rec(num):
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    return rec(num-1) + rec(num-2)
print(rec(int(input())))