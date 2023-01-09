import flet as ft

from TodoApp import TodoApp


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 700
    page.window_center()
    page.update()

    todo = TodoApp()

    page.add(todo)


ft.app(target=main)
