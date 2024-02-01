from functools import reduce
from math import gcd
def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def find_lcm_of_list(lst):
    return reduce(lcm, lst)
while True:
    
    print("Input")
    m, me = map(int, input("").split())
    if m==0 and me == 0:
        break
    mo = []
    me2 = []
    mayor = []
    menor=[]
    count = 0
    j = 0

    for i in range(m):
        mo.append(int(input()))
    for i in range(me):
        me2.append(int(input()))

    resultado = find_lcm_of_list(mo)
    
    x = resultado

    #   menor
    for i in range(me):
        j = 0
        while True:
            if j < me2[i]:
                j = j + x
            elif j > me2[i]:
                j=j-x
                menor.append(j)
                break
            elif j==me2[i]:
                menor.append(j)
                break
            else:
                print("")
    #mayor
    for i in range(me):
        j = 0
        while True:
            if j < me2[i]:
                j = j + x
            elif j >= me2[i]:
                mayor.append(j)
                break
            else:
                print("")
    print("Output")
    for i in range(me):
        print(f"{menor[i]} {mayor[i]}")
