from flet import FloatingActionButton, icons, Row, Column, Tab, Tabs, TextField, UserControl, Text, MainAxisAlignment, \
    CrossAxisAlignment, OutlinedButton, TextThemeStyle

from Task import Task


class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(
            hint_text="What needs to be done?",
            on_submit=self.add_clicked,
            expand=True)
        self.tasks = Column()

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="전체"), Tab(text="진행중"), Tab(text="완료")],
        )

        self.items_left = Text("0 items left")

        return Column(
            width=600,
            controls=[
                Row([Text(value="Todos", style=TextThemeStyle.HEADLINE_MEDIUM)], alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="완료된 사항 초기화", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                    status == "전체"
                    or (status == "진행중" and task.completed is False)
                    or (status == "완료" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()

    def tabs_changed(self, e):
        self.update()
