class NumNome:

    def __init__ (self, nome):
        self.nome = nome
    
    def __str__(self):
        return "Nome: %s\n" %(self.nome)

    def separar(self):
        letras = list(self.nome.upper())
        vogais = []
        consoantes = []
        
        for i in letras:
            if i in ["A", "E", "I", "O", "U"]:
                vogais.append(i)
            else:
                if i != ' ':
                    consoantes.append(i)

        dic = {
            'total': letras,
            'vogais': vogais,
            'consoantes': consoantes 
        }

        return dic

    def calcular(self, listaCaracteres):
        soma = 0
        for i in listaCaracteres:
            if i in ['A', 'Á', 'Â', 'J', 'S']:
                soma = soma + 1
            elif i in ['B', 'K', 'T']:
                soma = soma + 2
            elif i in ['C', 'Ç', 'L', 'U', 'Ú']:
                soma = soma + 3
            elif i in ['D', 'M', 'V']:
                soma = soma + 4
            elif i in ['E', 'É', 'Ê', 'N', 'W']:
                soma = soma + 5
            elif i in ['F', 'O', 'Ó', 'Ô', 'X']:
                soma = soma + 6
            elif i in ['G', 'P', 'Y']:
                soma = soma + 7
            elif i in ['H', 'Q', 'Z']:
                soma = soma + 8
            elif i in ['I', 'Í', 'R']:
                soma = soma + 9

        return soma
        
    def reduzir(self, soma):
        reducao = 0
        somaStr = str(soma)
        tamanho = len(somaStr)
       
        while (tamanho > 0):
           
            for i in somaStr:
                reducao = reducao + int(i)
                tamanho = tamanho -1

        if len(str(reducao)) > 1 and reducao != 11 and reducao != 22 and reducao != 33:
            reducao = self.reduzir(reducao)
            return reducao
        else:
            return reducao
    
    
    def runNome(self, nome):
        nomeObj = NumNome(nome)
        dic = nomeObj.separar()
        v = nomeObj.calcular(dic['vogais'])
        c = nomeObj.calcular(dic['consoantes'])
        t = v+c
        
        valores = {
                    'CONSOANTE'  : nomeObj.reduzir(c),
                    'VOGAL'      : nomeObj.reduzir(v),
                    '':'',
                    'TOTAL'       : nomeObj.reduzir(t)
                  }

        return valores


'''
n = 'arthur de souza frota'
x= NumNome(n)
print (n)
#print (x.run())
input()
'''
