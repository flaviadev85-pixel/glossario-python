"""Microatividade 4: leitura de arquivo externo."""

from pathlib import Path

caminho = Path(__file__).with_name("loremipsum.txt")
arquivo = caminho.open("r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()
print("Conteúdo completo:\n", conteudo)

with caminho.open("r", encoding="utf-8") as arquivo:
    primeira_linha = arquivo.readline()
print("Primeira linha:", primeira_linha, end="")
print("Três primeiros caracteres:", conteudo[:3])

with caminho.open("r", encoding="utf-8") as arquivo:
    print("Leitura com with:\n", arquivo.read())

