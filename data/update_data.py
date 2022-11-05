from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel


class Example(MDApp):
    data_tables = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        self.num_row = int(1)
        self.text = "Modifier la colonne {} ".format(self.num_row)

        layout = MDFloatLayout()
        layout.add_widget(
            MDRaisedButton(
                text="Change a row",
                pos_hint={"center_x": 0.5},
                on_release=self.update_row,
                y=24,
            )
        )

        layout.add_widget(
            MDLabel(
                id="colonneIndicator",
                text=self.text,
                pos_hint={"center_x": 1, "center_y": 0.14},
            )
        )

        layout.add_widget(
            MDRaisedButton(
                text="Select row up",
                pos_hint={"center_x": 0.65},
                on_release=self.select_row_up,
                y=24,
            )
        )

        layout.add_widget(
            MDRaisedButton(
                text="Select row down",
                pos_hint={"center_x": 0.81},
                on_release=self.select_row_down,
                y=24,
            )
        )

        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=False,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(40)),
                ("Column 2", dp(40)),
                ("Column 3", dp(40)),
            ],
            row_data=[(f"{i + 1}", "1", "2", "3") for i in range(3)],
        )
        layout.add_widget(self.data_tables)

        return layout

    def update_row(self, instance_button: MDRaisedButton) -> None:
        self.data_tables.update_row(
            self.data_tables.row_data[self.num_row - 1],  # old row data
            [str(self.num_row), "A", "B", "C"],          # new row data
        )


    # les deux buttons sont ajouté par moi-même
    def select_row_up(self, instance_button: MDRaisedButton)-> None:

        if(self.num_row < int(self.data_tables.row_data[-1][0])):
            self.num_row = self.num_row + 1
            self.text = "Modifier la colonne {} ".format(self.num_row)
            print(self.num_row)

    def select_row_down(self, instance_button: MDRaisedButton)-> None:

        if(self.num_row > 1):
            self.num_row = self.num_row - 1
            self.text = "Modifier la colonne {} ".format(self.num_row)
            print(self.num_row)


Example().run()