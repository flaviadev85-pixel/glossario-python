"""Microatividade 1: ordenação com o método nativo sort."""

numeros = [42, 7, 19, 3, 88, 14, 65, 1, 27, 51, 9, 73, 34, 6, 20]
numeros.sort()
print("Números em ordem crescente:", numeros)
numeros.sort(key=None, reverse=True)
print("Números em ordem decrescente:", numeros)

pessoas = [
    {"nome": "Carla", "dataNascimento": "1995-02-18", "cpf": "333", "rg": "30"},
    {"nome": "Ana", "dataNascimento": "2000-07-10", "cpf": "111", "rg": "10"},
    {"nome": "Bruno", "dataNascimento": "1988-11-03", "cpf": "222", "rg": "20"},
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])
print("Pessoas por nome crescente:", pessoas)
pessoas.sort(key=lambda pessoa: pessoa["nome"], reverse=True)
print("Pessoas por nome decrescente:", pessoas)

nomes = ["Carla", "Ana", "Bruno", "Daniela", "Eduardo"]
nomes.sort()
print("Strings em ordem crescente:", nomes)
nomes.sort(key=None, reverse=True)
print("Strings em ordem decrescente:", nomes)

