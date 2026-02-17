n = int(input())
for i in range(n):
    num = int(input())
    #Esto equivale
    # for j in range(num):
    #     valor = map(int, input().split())
    #     lista.append(tuple(valor))
    # a esto
    lista = [tuple(map(int, input().split())) for _ in range(num)]

    # Encuentra los valores clave mas de 3 valores
    # mayor0 = max(t[0] for t in lista)
    # menor1 = min(t[1] for t in lista if t[0] == mayor0)
    # mayor2 = max(t[2] for t in lista if t[0] == mayor0 and t[1] == menor1)

    # Paso 1: encontrar el mayor primer elemento
    mayor = max(t[0] for t in lista)

    # Paso 2: encontrar el menor segundo elemento entre los que tienen el primer elemento mayor
    menor = min(t[1] for t in lista if t[0] == mayor)

    # Paso 3: encontrar el mayor tercer elemento entre los que cumplen los dos anteriores
    emayor = max(t[2] for t in lista if t[0] == mayor and t[1] == menor)

    # Paso 4 Opcion 1: filtrar la(s) tupla(s) que cumplen las tres condiciones
    # resultado = [t for t in lista if t[0] == mayor and t[1] == menor and t[2] == emayor]

    # Paso 4 Opcion 2: imprimir la primera tupla que cumpla las tres condiciones
    for t in lista:
        if t[0] == mayor and t[1] == menor and t[2] == emayor:
            # imprime la tupla en numeros con espacios
            print(*t)
            # salimos del bucle para imprimir solo una vez
            break
# Priorizando Equipos
