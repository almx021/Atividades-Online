"""
5. Considere uma pilha que armazene caracteres. Faça uma função para determinar se
uma string é da forma XY, onde X é uma cadeia formada por caracteres arbitrários e Y é
o reverso de X. Por exemplo, se x = ABCD, então y = DCBA. Considere que x e y são
duas strings distintas.
"""

class Pilha(object):
    def __init__(self):
      self.items = []

    def adicionar(self, item):
        for elemento in item:
            self.items.append(elemento)

    def retirar(self):
        if not self.estaVazio():
            return self.items.pop()
        raise Exception

    def tamanho(self):
        return len(self.items)

    def estaVazio(self):
        return self.tamanho() == 0
    
    def topo(self):
        return self.items[-1]


def estaNoModeloXY(p1: object):
    if p1.tamanho() % 2 != 0 or p1.estaVazio():
        return "Nao está no modelo XY"
    
    p2 = Pilha()
    
    for _ in range(p1.tamanho() // 2):
        p2.adicionar(p1.topo())
        p1.retirar()
        
        # pilha1 = A B B A =>

        # pilha1 = A B B
        # pilha2 = A

        # pilha1 = A B
        # pilha2 = A B

    while not p2.estaVazio():
        if p1.topo() == p2.topo():
            p1.retirar()
            p2.retirar()

        else: 
            return "Nao esta no modelo XY"
    return "Esta no modelo XY"

palavra = input()

pilha1 = Pilha()

pilha1.adicionar(palavra)

print(pilha1.items)

print(estaNoModeloXY(pilha1))
