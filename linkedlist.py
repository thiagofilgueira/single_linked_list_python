from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0

  def append(self, value):
    if self.head:
      # inserção quando a lista não é vazia
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next = Node(value)
    else:
      # primeira inserção
      self.head = Node(value)
    self._size += 1

  def __len__(self):
    return self._size
  
  def get(self, index):
    # x = lista.get(3)
    pass

  def set(self, index, value):
    # lista.set(3, 6)
    pass

  # sobrecarga de operador
  def __getitem__(self, index):
    # x = lista[3]
    pointer = self.head
    for _ in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("List index out of range")
    if pointer:
      return pointer.data
    raise IndexError("List index out of range")
  
  def __setitem__(self, index, value):
    # lista[3] = 6
    pointer = self.head
    for _ in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("List index out of range")
    if pointer:
      pointer.data = value
    raise IndexError("List index out of range")

  # busca linear
  def index(self, value):
    """Retorna o indice do elemento"""
    pointer = self.head
    index = 0
    while pointer:
      if pointer.data == value:
        return index
      pointer = pointer.next
      index += 1
    raise ValueError("Value {} not found".format(value))
