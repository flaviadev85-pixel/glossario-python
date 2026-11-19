"""Microatividade 2: implementação do Bubble Sort."""


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporario = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporario


numeros = [42, 7, 19, 3, 88, 14, 65, 1, 27, 51, 9, 73, 34, 6, 20]
bubbleSort(numeros)
print(numeros)

