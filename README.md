# Lista Encadeada Simples (Single Linked List)


# Linked List

A classe LinkedList representa a lista encadeada.

## Método **init**

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

```

O método inicializador cria uma lista encadeada vazia, onde `self.head` é a referência para o primeiro nó da lista (inicialmente `None`), e `_size` armazena o número de elementos na lista (inicialmente 0).

## Método append

```python
def append(self, value):
    if self.head:
        pointer = self.head
        while(pointer.next):
            pointer = pointer.next
        pointer.next = Node(value)
    else:
        self.head = Node(value)
    self._size += 1

```

Este método adiciona um elemento ao final da lista. Se a lista não estiver vazia, ele percorre os nós até o final e adiciona um novo nó com o valor fornecido. Se a lista estiver vazia, cria o primeiro nó.

## Método **len**

```python
def __len__(self):
    return self._size

```

Este método retorna o tamanho da lista, ou seja, o número de elementos na lista.

## Métodos **getitem** e **setitem**

```python
def __getitem__(self, index):
    # Implementação para acessar um elemento pelo índice

def __setitem__(self, index, value):
    # Implementação para definir o valor de um elemento pelo índice

```

Esses métodos permitem acessar e definir valores na lista usando a notação de colchetes. Eles realizam uma busca linear pelos nós até o índice desejado e acessam ou definem o valor correspondente.

## Método index

```python
def index(self, value):
    # Implementação para encontrar o índice de um elemento na lista

```

Este método retorna o índice do primeiro elemento na lista que possui o valor fornecido. Realiza uma busca linear pela lista.

Esse código implementa uma lista encadeada simples e oferece métodos básicos para adicionar elementos, obter o tamanho, acessar e definir valores por índice, e encontrar o índice de um valor específico.

Aqui está um exemplo de uso da lista encadeada:

```python
# Criando uma nova lista encadeada
lista = LinkedList()

# Adicionando elementos à lista
lista.append(10)
lista.append(20)
lista.append(30)

# Imprimindo o tamanho da lista
print(len(lista))  # Saída: 3

# Acessando elementos por índice
print(lista[0])  # Saída: 10
print(lista[1])  # Saída: 20

# Definindo valores por índice
lista[2] = 40

# Imprimindo o índice de um elemento
print(lista.index(40))  # Saída: 2

```

Neste exemplo, uma lista encadeada é criada e elementos são adicionados a ela. O tamanho da lista é impresso, assim como o acesso a elementos específicos por índice. Um valor também é definido por índice, e o índice de um elemento é impresso usando o método `index`.