class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,value):
        if self.head: #se existe elementos na lista
            pointer = self.head #ponteiro para o primeiro elemento
            while(pointer.next): #enquanto existir um proximo elemento
                pointer = pointer.next #percorra meus elementos
            pointer.next = Node(value)    #ao chegar no fim, adicione o nó com o elemento no final da lista
        else:
            self.head = Node(value) #se nao existir elementos na lista, crie o primeiro elemento da lista, no caso apontando o head para o unico elemento existente
        self.size += 1

    def __len__(self):
        return self._size   
            

    def __getitem__(self,index):
        # a = lista[0]
        pointer = self._getnode(index) #ponteiro apontando para o primeiro elemento
        for _ in range(index): #para percorrer até o indice que passou como valor
            if pointer: #se o ponteiro nao for o ultimo elemento
                pointer = pointer.next # percorra atribuindo até o elemento do indice passado
            else:
                raise IndexError('erro') # caso o indice esteja fora dos padroes, levante o erro de index
        if pointer:
            return pointer.data
        else:
            raise IndexError('erro') #caso o ponteiro esteja apontando para o index passado, retorne o dado correspondente ao numero do nó
    def __setitem__(self,index,elem):
        # lista[0] = 4
        pointer = self._getnode(index) #ponteiro apontando para o primeiro elemento
        for _ in range(index): #para percorrer até o indice que passou como valor
            if pointer: #se o ponteiro nao for o ultimo elemento
                pointer = pointer.next # percorra atribuindo até o elemento do indice passado
            else:
                raise IndexError('erro') # caso o indice esteja fora dos padroes, levante o erro de index
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('erro') #caso o ponteiro esteja apontando para o index passado, retorne o dado correspondente ao numero do nó
        
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError('list index out of rangex')
        return pointer

    def index(self, elem):
        pointer = self.head
        i=0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError('{} is not in list'.format(elem))

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0: # transformo o elemento que quero inserir na estrutura de no
            node.next = self.head #o proximo elemento vai receber o primeiro elemento anterior antes dele entrar
            self.head = node  # a cabeca da lista passar a ser o novo 
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1 



""" testes
    def show(self):
        pointer = self.head
        while (pointer):
            print(pointer.data)
            pointer = pointer.next
"""


a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.show()