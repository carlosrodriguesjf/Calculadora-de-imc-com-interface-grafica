import flet as ft

def main(page: ft.Page):

    def botao_clicado(e):
        valor_peso = float(campo_peso.value)
        valor_altura = float(campo_altura.value)
        calculo_imc = (valor_peso * (valor_altura * valor_altura))/ 100000
        if calculo_imc > 40:
            resultado = f"Como seu IMC é maior do que 40 a sua situação é de Obesidade III (mórbida)"
            page.add(ft.Text(value=calculo_imc, size=20, color='red'))
            page.add(ft.Text(value=resultado, size=20, color='red'))


        campo_peso.clean()
        campo_altura.clean()


    btn = ft.ElevatedButton(text='Calcular IMC', on_click=botao_clicado)

    # Configurações da página
    page.title = "CALCULADORA DE IMC"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 300
    page.window.height = 400
    page.padding = ft.padding.only(top = 20, left = 20, right = 20)
    

    # campo peso
    campo_peso = ft.TextField(label='Digite seu peso em gramas', width=250)
    
    # campo peso
    campo_altura = ft.TextField(label='Digite sua altura', width=250)
    
    page.add(campo_peso, campo_altura, btn)
   


ft.app(main) 