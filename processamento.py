"""Leitura, normalização e escrita das palavras do glossário."""

import re
import unicodedata
from collections.abc import Iterable
from pathlib import Path

PADRAO_PONTUACAO = re.compile(r"[^\wÀ-ÿ'-]+", flags=re.UNICODE)


def normalizar_palavra(palavra: str) -> str:
    """Remove pontuação externa e padroniza a palavra em minúsculas."""
    palavra = unicodedata.normalize("NFC", palavra).casefold()
    return PADRAO_PONTUACAO.sub("", palavra).strip("_-' ")


def ler_palavras(caminho: str | Path) -> list[str]:
    """Lê um arquivo linha a linha e separa seu conteúdo em palavras."""
    palavras = list()
    with Path(caminho).open("r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            for item in linha.split():
                palavra = normalizar_palavra(item)
                if palavra:
                    palavras.append(palavra)
    return palavras


def remover_repeticoes(palavras: Iterable[str]) -> list[str]:
    """Mantém uma ocorrência de cada palavra sem ordenar o resultado."""
    return list(dict.fromkeys(palavras))


def escrever_palavras(caminho: str | Path, palavras: Iterable[str]) -> None:
    """Grava uma palavra por linha em UTF-8."""
    destino = Path(caminho)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8", newline="\n") as arquivo:
        for palavra in palavras:
            arquivo.write(f"{palavra}\n")

