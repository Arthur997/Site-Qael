class Arcano:

    def __init__ (self, nome):
        self.nome = nome
    
    def __str__(self):
        return "Nome: %s\n" %(self.nome)


    def calcular(self, listaCaracteres):
        soma = 0
        listaCaracteres = listaCaracteres.upper()

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
    
    
    def runNome(self, nome):
        

        soma = self.calcular(nome)
        carta = self.reduzir(soma)

        return carta



#n = 'nicole de souza frota '

#x= NumNome(n)
#y = x.runNome(n)
#print (y)
##print (x.run())
#input()

