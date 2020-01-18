from NumerologiaNome import NumNome
from NumerologiaAniversario import NumData

class Run():

    def run(self):
        print('===================================================================================')
        
        choice = input('1-Nome\n2-Idade\n3-Ambos\nO que deseja calcular? - ')
        
        while choice != '1' and choice != '2' and choice != '3':
            print('\nERROR! - Digite apenas a opcao (de 1 a 3)!\n')
            print('===================================================================================')
            choice = input('1-Nome\n2-Idade\n3-Ambos\nO que deseja calcular? - ')


        if (choice == '1'):
            inputNome = input('\nInsira o nome completo: ')
            nome = NumNome(inputNome)
            nomeReducao = nome.runNome(inputNome)
            print('===================================================================================')
            print(nome)
            print('Vogais: {} \nConsoantes: {}\nTotal: {}\n'.format(nomeReducao['vogais'],
                                                                    nomeReducao['consoantes'],
                                                                    nomeReducao['total']))
            print('===================================================================================')
            input('Digite qualquer tecla para finalizar.... ')
        
        elif(choice == '2'):
            inputData = input('\nInsira a data de nascimento:')
            data = NumData(inputData)
            dataReducao = data.runData(inputData)
            print('===================================================================================')
            print(data)
            print('Dia: {}\nMes: {}\nAno: {}\nTotal: {}'.format(dataReducao['dia'],
                                                                dataReducao['mes'],
                                                                dataReducao['ano'],
                                                                dataReducao['total']))
            print('===================================================================================')
            input('Digite qualquer tecla para finalizar.... ')

        elif(choice == '3'):
            inputNome = input('\nInsira o nome completo: ')
            inputData = input('Insira a data de nascimento:')
            data = NumData(inputData)
            nome = NumNome(inputNome)
            nomeReducao = nome.runNome(inputNome)
            dataReducao = data.runData(inputData)

            print('===================================================================================')
            print(nome)
            print('Vogais: {} \nConsoantes: {}\nTotal: {}\n'.format(nomeReducao['vogais'],
                                                                    nomeReducao['consoantes'],
                                                                    nomeReducao['total']))
            print(data)
            print('Dia: {}\nMes: {}\nAno: {}\nTotal: {}'.format(dataReducao['dia'],
                                                                dataReducao['mes'],
                                                                dataReducao['ano'],
                                                                dataReducao['total']))
            print('===================================================================================')
            input('Digite qualquer tecla para finalizar.... ')

        
x = Run
x.run(x)

        
