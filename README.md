# Glossário Jurídico Ordenado em Python

Trabalho prático da disciplina **DGT2819 — Persistência de Dados com Python**. O projeto lê um documento de texto linha a linha, separa e normaliza suas palavras, compara três formas de ordenação e grava um glossário em um novo arquivo `.txt`.

## Objetivos atendidos

- ordenação de listas com `list.sort()`;
- implementação manual de Bubble Sort;
- implementação manual de Selection Sort;
- leitura de arquivo externo com `with`;
- escrita dos dados processados em arquivo externo;
- medição do tempo de execução com `time.perf_counter()`;
- comparação dos resultados e da performance dos três métodos;
- geração do arquivo final com as palavras ordenadas;
- testes automatizados dos algoritmos e do processamento.

## Estrutura do projeto

```text
glossario-python/
├── algoritmos.py                 # Bubble, Selection e list.sort
├── processamento.py              # leitura, normalização e escrita
├── comparar_ordenacoes.py        # benchmark dos três métodos
├── kdd.py                        # programa final escolhido
├── dados/
│   └── texto_juridico.txt        # documento de entrada
├── resultados/
│   └── palavras_ordenadas.txt    # glossário gerado
├── microatividades/
│   ├── array.sort.py
│   ├── bubble.sort.py
│   ├── selection.sort.py
│   ├── ler.txt.py
│   ├── escrever.txt.py
│   └── loremipsum.txt
├── testes/
│   ├── test_algoritmos.py
│   └── test_processamento.py
└── docs/
    └── relatorio.md
```

## Como executar

O projeto utiliza apenas a biblioteca padrão do Python e não exige instalação de pacotes.

### 1. Comparar os algoritmos

```bash
python comparar_ordenacoes.py
```

Para aumentar o número de medições:

```bash
python comparar_ordenacoes.py dados/texto_juridico.txt --repeticoes 10
```

O programa imprime o tempo mediano de Bubble Sort, Selection Sort e `list.sort()`. Todos os métodos precisam produzir exatamente a mesma lista; caso contrário, a execução informa o problema.

### 2. Gerar o glossário final

```bash
python kdd.py
```

O resultado é salvo em `resultados/palavras_ordenadas.txt`, com uma palavra por linha. Para preservar ocorrências repetidas:

```bash
python kdd.py --manter-repeticoes
```

Também é possível informar outros arquivos:

```bash
python kdd.py caminho/entrada.txt caminho/saida.txt
```

### 3. Executar os testes

```bash
python -m unittest discover -s testes -v
```

### 4. Executar as microatividades

```bash
python microatividades/array.sort.py
python microatividades/bubble.sort.py
python microatividades/selection.sort.py
python microatividades/ler.txt.py
python microatividades/escrever.txt.py
```

## Fluxo de processamento

```text
arquivo TXT
    ↓ leitura linha a linha
separação com split()
    ↓
normalização em minúsculas e remoção de pontuação
    ↓
comparação: Bubble Sort × Selection Sort × list.sort()
    ↓ escolha do método nativo
remoção opcional de repetições
    ↓
palavras_ordenadas.txt
```

## Por que o método nativo foi escolhido?

Bubble Sort e Selection Sort têm complexidade quadrática, normalmente representada por **O(n²)**. Isso significa que o custo cresce rapidamente conforme aumenta a quantidade de palavras. O `list.sort()` do Python usa o algoritmo Timsort, otimizado e implementado internamente, com comportamento típico **O(n log n)**. Nos testes deste projeto ele também apresentou o menor tempo mediano.

O arquivo `comparar_ordenacoes.py` mantém os três algoritmos para fins acadêmicos e comparação. O programa final `kdd.py` usa somente o método escolhido, conforme a última etapa do enunciado.

## Decisões de implementação

- cada algoritmo recebe os dados e retorna uma nova lista, evitando alterar a entrada original;
- a leitura ocorre dentro de `with`, garantindo fechamento automático do arquivo;
- `split()` realiza a separação inicial exigida pelo enunciado;
- sinais de pontuação são removidos e as palavras são padronizadas em minúsculas;
- caracteres acentuados são preservados;
- o glossário final remove repetições para representar uma coleção de termos;
- os arquivos são lidos e gravados explicitamente em UTF-8;
- `perf_counter()` foi escolhido por sua precisão para medir intervalos curtos;
- a mediana de várias execuções reduz a influência de oscilações ocasionais.

## Exemplo de saída

```text
Palavras lidas: 74
Repetições por método: 5

Bubble Sort      0.000384100 segundo(s)
Selection Sort   0.000225600 segundo(s)
list.sort()      0.000006100 segundo(s)

Melhor mediana nesta execução: list.sort()
```

Esses valores foram obtidos na validação do projeto com sete repetições por método. Os tempos reais dependem do computador, do sistema operacional e da carga do momento.

