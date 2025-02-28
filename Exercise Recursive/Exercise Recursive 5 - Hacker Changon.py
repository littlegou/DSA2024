def rec(f,s):
    if f == s:
        print(s)
        return
    print(f)
    if f<=s:
        rec(f+1,s)
    else:
        rec(f-1,s)
rec(int(input()),int(input()))