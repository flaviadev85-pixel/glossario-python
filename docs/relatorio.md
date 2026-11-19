# Relatório técnico — Glossário Jurídico Ordenado

## 1. Contextualização

O projeto simula o primeiro MVP de um glossário destinado a evoluir para um dicionário de termos jurídicos. A entrada é um documento textual. A aplicação percorre o arquivo linha a linha, divide o conteúdo em palavras, normaliza os termos, compara estratégias de ordenação e persiste o resultado.

## 2. Algoritmos avaliados

### Bubble Sort

Compara elementos adjacentes e troca suas posições quando estão fora de ordem. A cada passagem, um dos maiores elementos é deslocado para o final. A implementação inclui uma interrupção antecipada quando uma passagem completa não realiza trocas.

### Selection Sort

Percorre a parte ainda não ordenada da lista, localiza o menor elemento e o troca com a posição inicial dessa região. Realiza poucas trocas, mas mantém o número quadrático de comparações.

### `list.sort()`

É o método nativo do Python. Utiliza Timsort, uma estratégia híbrida e estável que aproveita sequências previamente ordenadas. É a alternativa adequada para o programa final devido à performance, confiabilidade e legibilidade.

## 3. Metodologia da comparação

1. O mesmo arquivo e a mesma lista de palavras são usados nos três métodos.
2. Cada algoritmo trabalha sobre sua própria cópia da lista.
3. O cronômetro `perf_counter()` registra somente a etapa de ordenação.
4. Cada método é executado cinco vezes por padrão.
5. A mediana representa o tempo do método.
6. O programa valida que os três resultados sejam idênticos.

Tempos absolutos podem variar entre execuções. O objetivo é observar a tendência e relacioná-la à complexidade dos algoritmos.

## 4. Persistência em arquivo

A entrada é lida em UTF-8 com o gerenciador de contexto `with`. O resultado é gravado também em UTF-8, com uma palavra por linha. A pasta de destino é criada automaticamente quando necessário.

## 5. Resultado e conclusão

Os três métodos ordenam corretamente a mesma coleção. Para quantidades pequenas, todos concluem rapidamente; entretanto, Bubble Sort e Selection Sort aumentam o número de comparações de forma quadrática. O método nativo é o mais apropriado para o glossário final e permanece como única estratégia de ordenação em `kdd.py`. As implementações didáticas continuam disponíveis em `algoritmos.py` e no comparador para demonstrar os objetivos acadêmicos.

Na validação realizada com 74 palavras e sete repetições por método, as medianas observadas foram:

| Método | Tempo mediano |
|---|---:|
| Bubble Sort | 0,000384100 s |
| Selection Sort | 0,000225600 s |
| `list.sort()` | 0,000006100 s |

O glossário final foi gerado com 54 termos únicos. Como medições de intervalos muito curtos variam entre computadores, os números devem ser interpretados como um exemplo experimental, não como valores universais.

