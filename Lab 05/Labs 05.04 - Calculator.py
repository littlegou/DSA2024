n = int(input())
count = 0
for i in range(len(str(n))):
    count += n-int(0 if not i else i*"9")
print(count+n if n>1 else 1)