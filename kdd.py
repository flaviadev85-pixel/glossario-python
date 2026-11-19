"""MVP final: cria um glossário ordenado a partir de um documento de texto."""

from argparse import ArgumentParser
from pathlib import Path
from time import perf_counter

from algoritmos import sort_nativo
from processamento import escrever_palavras, ler_palavras, remover_repeticoes


def criar_glossario(
    origem: str | Path,
    destino: str | Path,
    manter_repeticoes: bool = False,
) -> tuple[list[str], float]:
    """Lê, ordena e grava as palavras; retorna resultado e tempo da ordenação."""
    palavras = ler_palavras(origem)
    if not manter_repeticoes:
        palavras = remover_repeticoes(palavras)

    inicio = perf_counter()
    ordenadas = sort_nativo(palavras)
    duracao = perf_counter() - inicio
    escrever_palavras(destino, ordenadas)
    return ordenadas, duracao


def main() -> None:
    parser = ArgumentParser(description="Cria um glossário de palavras ordenadas.")
    parser.add_argument("origem", nargs="?", default="dados/texto_juridico.txt")
    parser.add_argument("destino", nargs="?", default="resultados/palavras_ordenadas.txt")
    parser.add_argument(
        "--manter-repeticoes",
        action="store_true",
        help="mantém palavras repetidas no arquivo final",
    )
    argumentos = parser.parse_args()

    ordenadas, duracao = criar_glossario(
        argumentos.origem,
        argumentos.destino,
        argumentos.manter_repeticoes,
    )
    print(f"Glossário criado com {len(ordenadas)} palavra(s).")
    print(f"Tempo de ordenação: {duracao:.9f} segundo(s).")
    print(f"Arquivo gerado: {Path(argumentos.destino).resolve()}")
    print("\nPalavras ordenadas:")
    print(" | ".join(ordenadas))


if __name__ == "__main__":
    main()

