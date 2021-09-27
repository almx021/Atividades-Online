class Pilha(object):

    def __init__(self):
      self.__items = []

    def adicionar(self, item):
        self.__items.append(item)

    def remover(self):
        if not self.estaVazia():
            return self.__items.pop()
        raise IndexError("A pilha ja esta vazia!")
    
    def getItems(self):
        return self.__items

    def tamanho(self):
        return len(self.__items)

    def estaVazia(self):
        return self.tamanho() == 0

    def topo(self):
        return self.__items[-1]

def verificarPalindromo(palavra: str):

    pilha = Pilha()

    tamanhoPilha = len(palavra) // 2 if len(palavra) % 2 == 0 else len(palavra) // 2 + 1
    # palavra = a b b a -> tamanho = 4 -> tamanhoPilha = 2 -> pilha = a b
    # palavra = a b c b a -> tamanho = 5 -> tamanhoPilha = 3 -> pilha = a b c

    for i in range(tamanhoPilha):
        pilha.adicionar(palavra[i])

    for x in range(len(palavra) // 2, len(palavra)):
        if palavra[x] != pilha.topo():
            return print("Não é um palíndromo")
        pilha.remover()

    return print("É um palindromo")


entrada = input()
verificarPalindromo(entrada)
