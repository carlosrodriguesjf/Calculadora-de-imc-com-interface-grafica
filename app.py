import flet as ft

def main(page: ft.Page):


    def botao_clicado(e):
        
        valor_peso = float(campo_peso.value)
        valor_altura = float(campo_altura.value)
        calculo_imc = (valor_peso * (valor_altura * valor_altura))/ 100000

        if calculo_imc > 40:
            resultado = "Obesidade III (mórbida)"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#640000'))
            page.add(ft.Text(value=resultado, size=20, color='#640000'))

        elif calculo_imc >= 35:
            resultado = "Obesidade II (severa)"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#780000'))
            page.add(ft.Text(value=resultado, size=20, color='#780000'))

        elif calculo_imc >= 30:
            resultado = "Obesidade I"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#A00000'))
            page.add(ft.Text(value=resultado, size=20, color='#A00000'))

        elif calculo_imc >= 25:
            resultado = "Acima do peso"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#B40000'))
            page.add(ft.Text(value=resultado, size=20, color='#B40000'))

        elif calculo_imc >= 18.5:
            resultado = "Peso normal"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#D60000'))
            page.add(ft.Text(value=resultado, size=20, color='#D60000'))

        elif calculo_imc >= 17:
            resultado = "Abaixo do peso"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#FF0101'))
            page.add(ft.Text(value=resultado, size=20, color='#FF0101'))

        else :
            resultado = "Muito abaixo do peso"
            page.add(ft.Text(value=f"IMC = {calculo_imc}", size=20, color='#FBAFBC'))
            page.add(ft.Text(value=resultado, size=20, color='#FBAFBC'))


    # Configurações da página
    page.title = "CALCULADORA DE IMC"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 350
    page.window.height = 400
    page.padding = ft.padding.only(top = 20, left = 20, right = 20)

    # Configuração do campo peso
    campo_peso = ft.TextField(label='Digite seu peso em gramas', width=250)
    
    # Configuração do campo peso
    campo_altura = ft.TextField(label='Digite sua altura', width=250)

    # Configuração do botão
    btn = ft.ElevatedButton(text='Calcular IMC', on_click=botao_clicado)
    
    page.add(campo_peso, campo_altura, btn)
   

ft.app(main) 