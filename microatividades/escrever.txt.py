"""Microatividade 5: escrita de arquivo externo."""

from pathlib import Path

texto = list()
texto.append("Python permite ler e escrever arquivos.\n")
texto.append("O bloco with fecha o arquivo automaticamente.\n")
texto.append("Os dados podem ser persistidos para uso posterior.\n")

destino = Path(__file__).with_name("texto.txt")
with destino.open("w", encoding="utf-8") as arquivo:
    arquivo.writelines(texto)

print(f"Arquivo criado em: {destino}")

