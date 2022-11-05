from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                MDBoxLayout(
                    MDTextField(
                        hint_text="Date dd/mm/yyyy without limits",
                        helper_text="Enter a valid dd/mm/yyyy date",
                        validator="date",
                        date_format="dd/mm/yyyy",
                    ),
                    MDTextField(
                        hint_text="Date mm/dd/yyyy without limits",
                        helper_text="Enter a valid mm/dd/yyyy date",
                        validator="date",
                        date_format="mm/dd/yyyy",
                    ),
                    MDTextField(
                        hint_text="Date yyyy/mm/dd without limits",
                        helper_text="Enter a valid yyyy/mm/dd date",
                        validator="date",
                        date_format="yyyy/mm/dd",
                    ),
                    MDTextField(
                        hint_text="Date dd/mm/yyyy in [01/01/1900, 01/01/2100] interval",
                        helper_text="Enter a valid dd/mm/yyyy date",
                        validator="date",
                        date_format="dd/mm/yyyy",
                        date_interval=["01/01/1900", "01/01/2100"],
                    ),
                    MDTextField(
                        hint_text="Date dd/mm/yyyy in [01/01/1900, None] interval",
                        helper_text="Enter a valid dd/mm/yyyy date",
                        validator="date",
                        date_format="dd/mm/yyyy",
                        date_interval=["01/01/1900", None],
                    ),
                    MDTextField(
                        hint_text="Date dd/mm/yyyy in [None, 01/01/2100] interval",
                        helper_text="Enter a valid dd/mm/yyyy date",
                        validator="date",
                        date_format="dd/mm/yyyy",
                        date_interval=[None, "01/01/2100"],
                    ),
                    orientation="vertical",
                    spacing="20dp",
                    adaptive_height=True,
                    size_hint_x=0.8,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
        )


Test().run()