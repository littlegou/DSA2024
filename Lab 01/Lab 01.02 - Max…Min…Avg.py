"""Lab 01.02 - Max…Min…Avg"""
import json
def your_function(lis):
    """Lab 01.02 - Max…Min…Avg"""
    ma = lis[0]
    mi = lis[0]
    for i in lis[1:]:
        ma = i if i > ma else ma
        mi = i if i < mi else mi
    print((round(ma,2),round(mi,2),round(sum(lis)/len(lis),2)))
your_function(json.loads(input()))
