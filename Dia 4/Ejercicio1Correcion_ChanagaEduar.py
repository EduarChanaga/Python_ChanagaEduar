def pares(T_n, k):
    pairs = set()
    n = len(T_n)
    for i in range(n):
        for j in range(i + 1, n):
            if (T_n[i] + T_n[j]) % k == 0:
                pairs.add((T_n[i], T_n[j]))
    return pairs

T = int(input(" "))
found_pairs2 = []
for y in range(1, T + 1):

    n, k = map(int, input(" ").split())
    T_n = list(map(int, input(" ").split()))

    found_pairs = pares(T_n, k)

    if found_pairs:
        found_pairs2.append(len(found_pairs))
    else:
        print(" ")
for z in range(0, T, 1):
    print(f"Case #{z+1}: {found_pairs2[z]}")

## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647
## Desarrollado por Hernan Mendez Guerrero - 1101685607