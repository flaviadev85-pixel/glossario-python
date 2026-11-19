"""Algoritmos de ordenação utilizados no trabalho prático."""

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def bubble_sort(valores: Iterable[T]) -> list[T]:
    """Retorna uma nova lista ordenada pelo algoritmo Bubble Sort."""
    resultado = list(valores)
    tamanho = len(resultado)

    for i in range(tamanho):
        houve_troca = False
        for j in range(0, tamanho - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                houve_troca = True
        if not houve_troca:
            break

    return resultado


def selection_sort(valores: Iterable[T]) -> list[T]:
    """Retorna uma nova lista ordenada pelo algoritmo Selection Sort."""
    resultado = list(valores)

    for i in range(len(resultado)):
        indice_menor = i
        for j in range(i + 1, len(resultado)):
            if resultado[j] < resultado[indice_menor]:
                indice_menor = j
        resultado[i], resultado[indice_menor] = (
            resultado[indice_menor],
            resultado[i],
        )

    return resultado


def sort_nativo(valores: Iterable[T]) -> list[T]:
    """Retorna uma nova lista ordenada com o método nativo list.sort()."""
    resultado = list(valores)
    resultado.sort()
    return resultado

