class NumData():

    def __init__(self, data):
        self.data = data

        if self.data[2].isdigit():
            self.data = "0"+self.data
        
        if self.data[5].isdigit():
            self.data = self.data[:3] +'0'+self.data[3:]

    def __str__(self):
        return "Data: %s\n" % (self.data)
        
    def separar(self):
        
        numeros = []

        for i in self.data:
            if i.isdigit():
                numeros.append(int(i))

        separado = {
                    'dia': [numeros[0], numeros[1]],
                    'mes': [numeros[2], numeros[3]],
                    'ano': [numeros[4], numeros[5], numeros[6], numeros[7]]
                    }

        return separado  
                
    def calcular(self, separado):

        somaDia  = 0
        somaMes  = 0
        somaAno  = 0

        for i in separado['dia']:
            somaDia = somaDia + i

        for i in separado['mes']:
            somaMes = somaMes + i
        
        for i in separado['ano']:
            somaAno = somaAno + i

        somaTotal = somaDia + somaMes + somaAno

        dic = {
            'total': somaTotal,
            'dia': somaDia,
            'mes': somaMes,
            'ano': somaAno
        }

        return dic

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

    def runData(self, data):
        dataObj = NumData(data)
        dic = dataObj.separar()
        t   = dataObj.calcular(dic)
    
        valores = {
                    'DIA'  : dataObj.reduzir(t['dia']),
                    'MES'  : dataObj.reduzir(t['mes']),
                    'ANO'  : dataObj.reduzir(t['ano']),
                    'TOTAL': dataObj.reduzir(t['total'])
                }

        return valores

'''
n = "12-07-1997"
x = NumData(n)
print(n)
print (x.run())
'''