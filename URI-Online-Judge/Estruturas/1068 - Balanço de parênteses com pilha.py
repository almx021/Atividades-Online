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
    
def balancoDeParenteses(palavra: str):
    pilha = Pilha()

    for letra in palavra:
        if letra == '(':
            pilha.adicionar(letra)
        elif letra == ')':
            if pilha.estaVazia():
                return print('incorrect')
            pilha.remover()
    
    if pilha.estaVazia():
        return print('correct')
        
    return print('incorrect')

while True:
    try:
        entrada = input()
        balancoDeParenteses(entrada)
    except EOFError:
        break