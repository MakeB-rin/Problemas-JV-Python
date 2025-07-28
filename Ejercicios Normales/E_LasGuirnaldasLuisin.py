def contar(cadena):
    a = p = t = u = 0
    for c in cadena:
        if c == 'A':
            a += 1
        elif c == 'P':
            p += 1
        elif c == 'T':
            t += 1
        elif c == 'U':
            u += 1

    tap = min(t, a, p)
    t -= tap
    p -= tap
    tup = min(t, u, p)

    return tap + tup


cadena = input()
print(contar(cadena))
#Las Guirnaldas de Luisin
