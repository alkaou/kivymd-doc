from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            check=True,
            background_color_header="#65275d",
            background_color_cell="#451938",
            background_color_selected_cell="e4514f"
            # name column, width column, sorting function column(optional)
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),
                ("Column 3", dp(30)),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data=[
                (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
            ],
            elevation=2,
            rows_num=10,
            pagination_menu_height="140dp",
        )

        layout = AnchorLayout()
        layout.add_widget(self.data_tables)
        return layout
        


Example().run()