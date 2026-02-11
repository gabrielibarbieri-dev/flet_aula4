import flet as ft

def main(page: ft.page):
    page.title = "Meu app"
    page.add(
        ft.Text("Bem-vindo ap meu app!"),
        ft.Text("Eu me chamo Renan.")
    )
ft.app(main)