# Glossário Jurídico Ordenado em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Testes](https://img.shields.io/badge/testes-8%20aprovados-2EA44F)
![Dependências](https://img.shields.io/badge/dependências-apenas%20biblioteca%20padrão-6F42C1)
![Status](https://img.shields.io/badge/status-concluído-1F883D)

> Trabalho prático da disciplina **DGT2819 — Persistência de Dados com Python**.

Este projeto implementa um fluxo completo de processamento de texto: lê um documento jurídico linha a linha, extrai e normaliza seus termos, compara três estratégias de ordenação e grava um glossário alfabetizado em um novo arquivo TXT. A solução foi organizada em módulos, documentada e acompanhada de testes automatizados.

## Visão geral

O problema proposto envolve duas áreas fundamentais da programação com Python:

1. **persistência de dados**, por meio da leitura e escrita de arquivos externos;
2. **análise de algoritmos**, pela implementação e comparação de diferentes métodos de ordenação.

A aplicação utiliza Bubble Sort, Selection Sort e o método nativo `list.sort()`. Depois de validar que os três produzem o mesmo resultado, mede o tempo de execução de cada alternativa. O método nativo foi selecionado para o programa final por apresentar o melhor desempenho nos testes realizados.

## Requisitos atendidos

| Requisito do trabalho | Implementação | Situação |
|---|---|:---:|
| Ordenar uma lista com recurso nativo | `sort_nativo()` com `list.sort()` | ✅ |
| Implementar Bubble Sort | `bubble_sort()` | ✅ |
| Implementar Selection Sort | `selection_sort()` | ✅ |
| Ler arquivo TXT | `ler_palavras()` com gerenciador `with` | ✅ |
| Separar o texto em palavras | uso de `split()` durante a leitura | ✅ |
| Comparar os três métodos | `comparar_ordenacoes.py` | ✅ |
| Medir o tempo de execução | `time.perf_counter()` e mediana | ✅ |
| Escolher o método mais eficiente | `list.sort()` no programa final | ✅ |
| Escrever o resultado em outro TXT | `escrever_palavras()` | ✅ |
| Entregar as microatividades | pasta `microatividades/` | ✅ |
| Validar o comportamento | 8 testes automatizados | ✅ |

## Arquitetura da solução

O código foi separado por responsabilidade para facilitar leitura, manutenção e testes:

| Arquivo | Responsabilidade |
|---|---|
| `algoritmos.py` | implementa Bubble Sort, Selection Sort e ordenação nativa |
| `processamento.py` | concentra leitura, normalização, remoção de duplicados e escrita |
| `comparar_ordenacoes.py` | executa o benchmark e verifica a equivalência dos resultados |
| `kdd.py` | coordena o fluxo final e gera o glossário |
| `testes/` | valida algoritmos, normalização e persistência |
| `docs/relatorio.md` | apresenta a análise técnica da solução |

## Fluxo de processamento

```text
documento TXT de entrada
          │
          ▼
leitura segura linha a linha com with
          │
          ▼
separação inicial das palavras com split()
          │
          ▼
normalização: minúsculas + remoção de pontuação
          │
          ▼
Bubble Sort × Selection Sort × list.sort()
          │
          ▼
validação dos resultados + medição de desempenho
          │
          ▼
remoção opcional de termos repetidos
          │
          ▼
resultados/palavras_ordenadas.txt
```

## Estrutura do repositório

```text
glossario-python/
├── algoritmos.py
├── processamento.py
├── comparar_ordenacoes.py
├── kdd.py
├── pyproject.toml
├── dados/
│   └── texto_juridico.txt
├── resultados/
│   └── palavras_ordenadas.txt
├── microatividades/
│   ├── array.sort.py
│   ├── bubble.sort.py
│   ├── selection.sort.py
│   ├── ler.txt.py
│   ├── escrever.txt.py
│   ├── loremipsum.txt
│   └── texto.txt
├── testes/
│   ├── test_algoritmos.py
│   └── test_processamento.py
└── docs/
    └── relatorio.md
```

## Decisões técnicas

### Leitura e escrita seguras

Os arquivos são abertos com o gerenciador de contexto `with`, que garante o fechamento automático mesmo se ocorrer uma exceção. A codificação UTF-8 é informada explicitamente para preservar acentos e caracteres da língua portuguesa.

### Normalização dos termos

Antes da ordenação, cada palavra é convertida para minúsculas e tem sua pontuação periférica removida. Termos vazios são descartados e os caracteres acentuados são preservados. Essa etapa evita que `Contrato`, `contrato` e `contrato,` sejam tratados como entradas diferentes.

### Integridade dos dados

Cada algoritmo trabalha sobre uma cópia da lista recebida. Assim, a entrada original não é alterada e todos os métodos são comparados nas mesmas condições. O benchmark também verifica se as três saídas são idênticas antes de apresentar os tempos.

### Medição de desempenho

Foi utilizado `time.perf_counter()`, adequado para intervalos curtos. Cada método é executado diversas vezes e o valor apresentado é a mediana, reduzindo a interferência de oscilações ocasionais do sistema operacional.

## Análise dos algoritmos

| Método | Melhor caso | Caso médio | Pior caso | Memória adicional |
|---|---:|---:|---:|---:|
| Bubble Sort otimizado | O(n) | O(n²) | O(n²) | O(n)* |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(n)* |
| `list.sort()` / Timsort | O(n) | O(n log n) | O(n log n) | O(n) |

O Bubble Sort possui uma interrupção antecipada quando nenhuma troca acontece, o que melhora seu comportamento em listas já ordenadas. Ainda assim, tanto ele quanto o Selection Sort apresentam crescimento quadrático. O Timsort, usado internamente pelo Python, combina eficiência e aproveitamento de sequências parcialmente ordenadas.

\* Bubble Sort e Selection Sort podem operar em O(1) de memória auxiliar. Nesta implementação, O(n) é contabilizado porque cada função cria uma cópia para preservar a lista original.

## Resultado do benchmark

Validação realizada com **74 palavras** e sete repetições por método:

| Algoritmo | Tempo mediano observado |
|---|---:|
| Bubble Sort | 0,0003841 s |
| Selection Sort | 0,0002256 s |
| `list.sort()` | **0,0000061 s** |

Os tempos podem variar conforme o computador e a carga do sistema. O dado relevante é que, nas mesmas condições de execução, `list.sort()` apresentou a menor mediana e foi adotado em `kdd.py`.

## Como executar

### Pré-requisitos

- Python 3.10 ou superior;
- nenhum pacote externo é necessário.

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/flaviadev85-pixel/glossario-python.git
cd glossario-python
```

### Comparar os algoritmos

```bash
python comparar_ordenacoes.py
```

Para alterar o número de medições:

```bash
python comparar_ordenacoes.py dados/texto_juridico.txt --repeticoes 10
```

### Gerar o glossário final

```bash
python kdd.py
```

O resultado será salvo em `resultados/palavras_ordenadas.txt`, com um termo por linha. Para manter ocorrências repetidas:

```bash
python kdd.py --manter-repeticoes
```

Também é possível definir outros arquivos de entrada e saída:

```bash
python kdd.py caminho/entrada.txt caminho/saida.txt
```

### Executar os testes

```bash
python -m unittest discover -s testes -v
```

### Executar as microatividades

```bash
python microatividades/array.sort.py
python microatividades/bubble.sort.py
python microatividades/selection.sort.py
python microatividades/ler.txt.py
python microatividades/escrever.txt.py
```

## Qualidade e validação

- **8 testes automatizados aprovados**;
- três algoritmos validados com saídas equivalentes;
- leitura e escrita verificadas em UTF-8;
- tratamento de lista vazia, lista unitária, duplicados e dados já ordenados;
- scripts das microatividades executados individualmente;
- projeto baseado somente na biblioteca padrão do Python.

## Resultado produzido

O arquivo final contém **54 termos jurídicos únicos**, ordenados alfabeticamente e gravados com um termo por linha. A opção `--manter-repeticoes` permite gerar uma versão que conserva todas as ocorrências do documento original.

## Limitações e possíveis evoluções

O trabalho atende ao escopo solicitado, mas pode ser expandido futuramente com:

- interface gráfica ou aplicação web para envio de documentos;
- exportação do glossário para CSV ou banco de dados;
- processamento de documentos maiores em lotes;
- filtros de palavras irrelevantes (*stopwords*);
- ordenação linguística sensível a acentos e localidade;
- gráficos comparativos de desempenho.

## Conclusão

O projeto demonstra, de forma integrada, manipulação de listas, implementação de algoritmos, leitura e escrita de arquivos, medição de desempenho, modularização e testes. A comparação experimental confirma a vantagem do método nativo do Python para o fluxo final, enquanto as implementações manuais permitem compreender o funcionamento e o custo dos algoritmos clássicos de ordenação.

Para uma análise mais detalhada, consulte o [relatório técnico](docs/relatorio.md).
