"""Compara resultado e tempo dos três métodos de ordenação."""

from argparse import ArgumentParser
from collections.abc import Callable
from pathlib import Path
from statistics import median
from time import perf_counter

from algoritmos import bubble_sort, selection_sort, sort_nativo
from processamento import ler_palavras

Ordenador = Callable[[list[str]], list[str]]


def medir(ordenador: Ordenador, palavras: list[str], repeticoes: int) -> tuple[list[str], float]:
    """Executa o ordenador várias vezes e retorna a mediana dos tempos."""
    tempos = []
    resultado = []
    for _ in range(repeticoes):
        inicio = perf_counter()
        resultado = ordenador(palavras)
        tempos.append(perf_counter() - inicio)
    return resultado, median(tempos)


def comparar(caminho: str | Path, repeticoes: int = 5) -> dict[str, float]:
    """Compara os algoritmos e garante que todos produzam o mesmo resultado."""
    palavras = ler_palavras(caminho)
    metodos: dict[str, Ordenador] = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "list.sort()": sort_nativo,
    }
    tempos = {}
    referencia = None

    print(f"Palavras lidas: {len(palavras)}")
    print(f"Repetições por método: {repeticoes}\n")
    for nome, metodo in metodos.items():
        resultado, tempo = medir(metodo, palavras, repeticoes)
        if referencia is None:
            referencia = resultado
        elif resultado != referencia:
            raise RuntimeError(f"O método {nome} produziu resultado divergente.")
        tempos[nome] = tempo
        print(f"{nome:<16} {tempo:.9f} segundo(s)")

    vencedor = min(tempos, key=tempos.get)
    print(f"\nMelhor mediana nesta execução: {vencedor}")
    return tempos


def main() -> None:
    parser = ArgumentParser(description="Compara algoritmos de ordenação de palavras.")
    parser.add_argument("arquivo", nargs="?", default="dados/texto_juridico.txt")
    parser.add_argument("--repeticoes", type=int, default=5)
    argumentos = parser.parse_args()
    if argumentos.repeticoes < 1:
        parser.error("--repeticoes deve ser maior que zero")
    comparar(argumentos.arquivo, argumentos.repeticoes)


if __name__ == "__main__":
    main()

