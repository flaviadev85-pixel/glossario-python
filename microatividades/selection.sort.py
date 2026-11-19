"""Microatividade 3: implementação do Selection Sort."""

numeros = [42, 7, 19, 3, 88, 14, 65, 1, 27, 51, 9, 73, 34, 6, 20]

for i in range(len(numeros)):
    indice_menor = i
    for j in range(i + 1, len(numeros)):
        if numeros[indice_menor] > numeros[j]:
            indice_menor = j
    numeros[i], numeros[indice_menor] = numeros[indice_menor], numeros[i]

print(numeros)

