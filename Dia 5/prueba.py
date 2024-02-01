from functools import reduce
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def find_lcm_of_list(lst):
    return reduce(lcm, lst)

def find_gcd_of_list(lst):
    return reduce(gcd, lst)

while True:
    print("Input")
    m, me = map(int, input("").split())
    
    if m == 0 and me == 0:
        break
    
    mo = []
    me2 = []
    
    for i in range(m):
        mo.append(int(input()))
    
    for i in range(me):
        me2.append(int(input()))

    lcm_mo = find_lcm_of_list(mo)
    gcd_me2 = find_gcd_of_list(me2)

    print("Resultado MCM:", lcm_mo)
    print("Resultado MCD:", gcd_me2)


