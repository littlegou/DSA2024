import json
import time
def isIntersect(a, b, c):
    stime = time.time()
    for i in a:
        if i in b and i in c:
            print(True)
            return
    print(False)
    etime = time.time()
    print(etime-stime)
isIntersect(json.loads(input()), json.loads(input()), json.loads(input()))