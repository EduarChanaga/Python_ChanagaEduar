def pares(T_n, n, k):
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            if (T_n[i] + T_n[j]) % k == 0:
                pairs.add((min(T_n[i], T_n[j]), max(T_n[i], T_n[j])))
              
    return len(pairs)

T = int(input("Ingrese el número de casos: "))
for case in range(1, T+1):
    n, k = map(int, input().split())
    T_n = list(map(int, input().split()))
    result = pares(T_n, n, k)
    print(f"Case {case}: {result}")

 

## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647
## Desarrollado por Hernan Mendez Guerrero - 1101685607