import flet as ft


def main(page: ft.Page):
    page.title="App004"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER  
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="purple"
    page.add(
        ft.column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
                ],alignment="center")
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMult,
            btnDiv,
            btnLimpiar,
            ],alignment="center")
    )
btnSuma=ft.ElevatedButton(
    "+",
    color="black",
    width=100,
    height=50)
ft.app(main)
