# 10/01/2024 # 
# Projeto: Calculadora de Imposto de Renda #

# Projeto para praticar as estuturas if, elif, else #


# Anotações 
# == igualdade: verifica se dois valores são iguais
# != diferença: verifica se dois valores são diferentes 
# < >= 


# entrada de dados

print('''==============================================
      Calculadora de Imposto de Renda
==============================================\n''')

Nome = input('Por favor digite seu nome: ')
print(f'\nOlá {Nome}, responda as perguntas á seguir para calcularmos seu IR!\n')

while True:

    try:
        RendaAnual = float(input("\nPor favor informe sua renda anual em reais(apenas números): "))
        if RendaAnual > 0: 
            break

        else:
            print('\nA renda anual deve ser um número positivo')
            
    except:
        print('\nEntrada inválida. Por favor digite apenas numeros')
                
while True:
    try:
        DespesaMedica = input('\nVocê possui despesas médicas comprovadas(sim ou não): ').strip().lower()
        if DespesaMedica == 'sim' or DespesaMedica == 'não' or DespesaMedica == 'nao': 
            break
        else: 
            print('\nPor favor digite uma resposta válida.')
    except ValueError:
        print('\nEntrada inválido, por favor digite sim ou não')


while True:
# .strip() remove os espaços em branco .lower() deixa todas as letras minusculas 
    try:        
        Estudante = input('\nVocê é estudante(sim ou não): ').strip().lower()  
        if Estudante == 'sim' or Estudante == 'não' or Estudante == 'nao':
            break
        else:
            print('Por favor digite uma resposta válida.')
    except ValueError:
        print('Erro, por favor digite sim ou não.')


Limite = 22847.76

Imposto1 = 0.075
Imposto2 = 0.15
Imposto3 = 0.225
Imposto4 = 0.275

DescontoMedico = 0.05
DescontoEstudante = 5000

    
# cálculo do imposto 

if RendaAnual <= Limite: 
    print('\nVocê está isento do imposto de renda! :)')

else:
    Excedente = RendaAnual - Limite

    if 22847.77 < RendaAnual <= 33919.80:
        Imposto = Excedente * Imposto1
        # verifica se o usuario teve despesa médicas e faz o cálculo  
    

    elif 33919.81 < RendaAnual <= 45012.60:
        Imposto = Excedente * Imposto2
        

    elif 45012.61 < RendaAnual <= 55976.16:
        Imposto = Excedente * Imposto3

    else:
        Imposto = Excedente * Imposto4

    if DespesaMedica == "sim":
        Imposto -= Imposto* DescontoMedico
        
    if Estudante == 'sim':
        Imposto-= DescontoEstudante





    Imposto = max(0, Imposto) # max() garante que o imposto nunca será negativo, inferior a 0 
    print (f'\nSeu imposto de renda é: {Imposto:.2f}')

    ImpostoSemDesconto = Excedente * (Imposto1 if RendaAnual <= 33919.80 else 
                                      Imposto2 if RendaAnual <= 45012.60 else 
                                      Imposto3 if RendaAnual <= 55976.16 else Imposto4)
    

    print(f'\nSeu imposto sem os descontos seria de: {ImpostoSemDesconto:.2f}')



