- Complexidade de tempo: Total: O(n^2). Detalhado: O(n^2) p/ ordenação e O(log n) p/ busca ordenada.
- Complexidade de espaço: O(1) -> Tanto a ordenação quanto à busca não requerem espaço adcional significativo que impacte a performance da execução do programa.

# Perfomance

- Complexity: Total: O(n^2)
    - O(n^2) p/ bubble sorting 
    - O(log n) p/ busca ordenada.


# Code
```python
def busca_ordenada(lista, elemento) -> int:

    def bubble_sort(lista):
      n = len(lista)
      for i in range(n):
          trocado = False
          for j in range(0, n-i-1):
              if lista[j] > lista[j+1]:
                  lista[j], lista[j+1] = lista[j+1], lista[j]
                  trocado = True
          if not trocado:
              break
      return lista

    lista = bubble_sort(lista)

    # define as variáveis prev e next com valor inicial igual às extremidades da lista
    prev, next = 0, len(lista) - 1

    # se a variável prev ficar maior que a next, significa que toda a lista já foi comparada e o elemento não foi encontrado
    while prev <= next:
      middle_idx = (prev + next) // 2
      middle_element = lista[middle_idx]

      if middle_element == elemento:
          return middle_idx
      elif middle_element < elemento:
          prev = middle_idx + 1
      else:
          next = middle_idx - 1

    return -1
```