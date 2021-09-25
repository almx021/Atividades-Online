class Pilha(object):
    def __init__(self):
      self.items = ["F A C E"]

    def adicionar(self, item):
        self.items.append(item)

    def retirar(self):
        if not self.estaVazio():
            return self.items.pop()
        raise Exception

    def estaVazio(self):
        return len(self.items) == 0
    
    def topo(self):
        return self.items[-1]


n = int(input())
contador = 0

pilha = Pilha()

while n > 0:
    texto = input()

    #[::-1] inverte o elemento
    if texto == pilha.topo()[::-1]:
        pilha.retirar()
        
        if pilha.estaVazio():
            pilha.adicionar("F A C E")
        
        contador += 1
    
    else:
        pilha.adicionar(texto)
    n -= 1

print(contador)