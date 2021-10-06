class Pilha(object):
    def __init__(self):
      self.__items = ["F A C E"]

    def adicionar(self, item):
        self.__items.append(item)

    def remover(self):
        if not self.estaVazia():
            return self.__items.pop()
        raise IndexError

    def estaVazia(self):
        return len(self.__items) == 0
    
    def topo(self):
        return self.__items[-1]


n = int(input())
contador = 0

pilha = Pilha()

while n > 0:
    palavra = input()

    #[::-1] inverte o elemento
    if palavra == pilha.topo()[::-1]:
        pilha.remover()
        
        if pilha.estaVazia():
            pilha.adicionar("F A C E")
        
        contador += 1
    
    else:
        pilha.adicionar(palavra)
        
    n -= 1

print(contador)