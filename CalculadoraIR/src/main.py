import flet as ft




def main(page: ft.Page):
    page.title = 'Calculadora de Imposto de Renda'
    page.theme_mode = 'dark'
    page.window.width = 400
    page.window.height = 700
    
    
    Limite = 22847.76

    Imposto1 = 0.075
    Imposto2 = 0.15
    Imposto3 = 0.225
    Imposto4 = 0.275

    DescontoMedico = 0.05
    DescontoEstudante = 5000
    
    campo_entrada = ft.TextField(label='Digite sua renda anual')

    resultado_texto = ft.Text(value='', color='black', )
        
    def CalcularImposto(e):

        RendaAnual = campo_entrada.value # captura o valor do campo 
        if not RendaAnual.strip(): # verifica se o campo está vazio 
            resultado_texto.value = 'Erro o campo está vazio.'
            resultado_texto.color = 'red'
            page.update()
            return
        
        try:
            RendaAnual = float(RendaAnual) # tenta conveter para numero
            if RendaAnual > 0:
                resultado_texto.value = f'Entrada válida {RendaAnual}'
                resultado_texto.color = 'green'
                page.RendaAnual = RendaAnual

            else:
                resultado_texto.value = 'Erro, o valor deve ser maior que zero'
                resultado_texto.color = 'Red'
        except ValueError:
            resultado_texto.value = 'Erro, entrada inválida. Insira apenas números'
            resultado_texto.color = 'Red'
            page.update()
            return
        # atualiza a página 
        page.update()

   

    
        DespesasMedicas = DespesasMedicasCB.value
        Estudante = EstudanteCB.value

        if Estudante is None or DespesasMedicas is None: 
            resultado_textoCB.value = 'Erro, você tem que selecionar uma das opções'
            resultado_textoCB.color = 'red'
            page.update()
            return
     

    
        else:
            if RendaAnual <= Limite: 
                Imposto = 0
                mensagem = f'Você está isento do imposto de renda! :)'
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

                if DespesasMedicas == "Sim":
                    Imposto -= Imposto * DescontoMedico
                    
                if Estudante == 'Sim':
                    Imposto -= DescontoEstudante

                Imposto = max(0, Imposto) # max() garante que o imposto nunca será negativo, inferior a 0 
                mensagem = f'Seu imposto de renda é: {Imposto:.2f}'

                ImpostoSemDesconto = Excedente * (Imposto1 if RendaAnual <= 33919.80 else 
                                      Imposto2 if RendaAnual <= 45012.60 else 
                                      Imposto3 if RendaAnual <= 55976.16 else Imposto4)
    
                mensagem2 = f'Seu imposto sem os descontos seria de: {ImpostoSemDesconto:.2f}'

              

        resultado_textoCB.value = mensagem
        resultado_textoCB.color = 'green'
        resultado_desconto.value = mensagem2
        resultado_desconto.color = 'green'
        page.update()
         
    
    
    DespesasMedicasCB = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value='Sim', label='Sim'), 
            ft.Radio(value='Não', label='Não')
        ]), 
    )

    EstudanteCB = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value='Sim', label='Sim'), 
            ft.Radio(value='Não', label='Não')
        ]), 
    )

    BotaoConfirmar = ft.ElevatedButton(text='Calcular',
                                       on_click=CalcularImposto)

    resultado_textoCB = ft.Text(value='', color='black')

    resultado_desconto = ft.Text(value='', color='black' )

    page.add(
            campo_entrada,
            resultado_texto,
            ft.Text(value='Você é estudante?'),
            EstudanteCB,
            ft.Text('Você tem despesas médicas?'),
            DespesasMedicasCB,
            resultado_textoCB, 
            BotaoConfirmar,
            resultado_desconto,
            
    )
    
    
ft.app(main)
