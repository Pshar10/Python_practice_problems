import numpy as np

a = [1,2,3,4]
b  = [1 ,2,5,4]

def chk_eql(a,b):
    return "matching" if all(i==j for i,j in zip(a,b)) else "not matching"

str = chk_eql(a,b)

print(str)
