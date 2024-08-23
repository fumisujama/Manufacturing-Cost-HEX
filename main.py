import flet as ft

def main(page: ft.Page):
    a=ft.Text("hello world")

    page.controls.append(a)
    page.update()

ft.app(target=main)
