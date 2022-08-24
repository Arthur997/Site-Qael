class Arcano:

    def __init__ (self, nome, destino=0):
        self.nome = nome
        self.destino = destino
    
    def __str__(self):
        return "Nome: %s\n" %(self.nome)


    def calcularComum(self):
        soma = 0
        listaCaracteres = self.nome.upper()

        tabela = {'A' : 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                    'F' : 6, 'G': 7, 'H': 8, 'I': 9, 'J': 9,
                    'K' : 10, 'L': 20, 'M': 30, 'N': 40, 'O': 50,
                    'P' : 60, 'Q': 70, 'R': 80, 'S': 90, 'T': 100,
                    'U' : 200, 'V': 200, 'W': 200, 'X': 300, 'Y': 9,
                    'Z' : 400, 'Ã': 41, 'Õ': 90, ' ': 0, 'É': 5, 'Í': 9,
                    'Á' : 1, 'Ó': 50, 'Ú': 200, "'": 0, 'Ê': 5, 'Ô': 50, 
                    'Ç' : 3, 'Â': 1
                    } 
        
        for i in listaCaracteres:
            soma = soma + tabela[i]

        return soma
    
    def calcularBatismo(self):
        listaCaracteres = self.nome
        soma = 0
        
        for i in listaCaracteres:
            if i in ['A', 'a', 'j', 'J', 't', 'T']:
                soma = soma + 1
            elif i in ['B', 'b', 'L', 'l', 'U', 'u']:
                soma = soma + 2
            elif i in ['C', 'c', 'M', 'm', 'V', 'v']:
                soma = soma + 3
            elif i in ['D', 'd', 'N', 'n', 'X', 'x']:
                soma = soma + 4
            elif i in ['E', 'e', 'Ø', 'ø', 'Y', 'y']:
                soma = soma + 5
            elif i in ['F', 'f', 'P', 'p', 'Z', 'z']:
                soma = soma + 6
            elif i in ['G', 'g', 'Q', 'q', 'æ', 'Æ']:
                soma = soma + 7
            elif i in ['H', 'h', 'R', 'r']:
                soma = soma + 8
            elif i in ['I', 'i', 'S', 's']:
                soma = soma + 9
            elif i == ' ':
                soma = soma + 0
            else:
                raise Exception

        return soma
        
    def reduzir(self, soma):
        
        if (soma not in range(1,23)):
            reducao = 0
        else: reducao = soma

        somaStr = str(soma)
        tamanho = len(somaStr)

        while (reducao not in range(1,23)):

            for i in somaStr:
                reducao = reducao + int(i)
                tamanho = tamanho -1

        if reducao not in range(1,23):
            reducao = self.reduzir(reducao)
            return reducao
        else:
            return reducao
    
    def runArcano(self):
        destino = self.destino
        
        if destino == 0:
            soma = self.calcularComum()
            carta = self.reduzir(soma)
        else:
            soma = self.calcularBatismo()
            redNome = self.reduzir(soma)
            carta = self.reduzir(redNome + destino)

        return carta

# n = 'Øa shemih fa'
# d = 9
# x= Arcano(n,d)
# y = x.runArcano()
# print (y)