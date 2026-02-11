import flet as ft

def main(page: ft.page):
    page.bgcolor = "#93bbfa"
    page.vertical_aligment = ft.MainAxisAlignment.CENTER
    page.horizontal_aligment = ft.CrossAxisAlignment.CENTER
    def mostrar_mensagem(e):
        page.add(ft.Text("A NÃO, VOCÊ FOI CONGELADO!"))

    page.add (
        ft.Text("Olá, meu nome é Frozen!", bgcolor="blue"),
        ft.Image(
            src="images/Frozen.jpg",
            height=200
        ),
        ft.Button(
            content="Poder de congelamento",
            on_click=mostrar_mensagem
           
        )
    )

ft.app(main)