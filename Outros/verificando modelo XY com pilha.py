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
        self.items.append(item)

    def adicionarPalavra(self, palavra):
        for letra in palavra:
            self.items.append(letra)

    def remover(self):
        if not self.estaVazio():
            return self.items.pop()
        raise IndexError("A pilha ja esta vazia!")

    def getItems(self):
        return self.__items

    def tamanho(self):
        return len(self.items)

    def estaVazio(self):
        return self.tamanho() == 0
    
    def topo(self):
        return self.items[-1]

def estaNoModeloXY(palavra: str):
    if len(palavra) % 2 != 0 or palavra == '':
        return print("Nao esta no modelo XY")


    # Desnecessario, mas fiz isso por fins didáticos
    x = palavra[:len(palavra) // 2] # x = primeira metade da palavra
    y = palavra[len(palavra) // 2:] # y = segunda metade da palavra

    p1 = Pilha()
    p1.adicionarPalavra(y)

    for letra in x:
        if letra == p1.topo():
            p1.remover()
        else:
            return print("Nao esta no modelo XY")

    return print("Esta no modelo XY")

entrada = input()

estaNoModeloXY(entrada)
