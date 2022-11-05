from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                MDFloatingActionButtonSpeedDial(
                    data={
                        "Python": "language-python",
                        "JS": [
                            "language-javascript",
                            "on_release", lambda x: self.callback,
                        ],
                        "PHP": [
                            "language-php",
                            "on_release", lambda x:  self.callback,
                        ],
                        "C++": [
                            "language-cpp",
                            "on_release", lambda x:  self.callback,
                        ],
                    },
                    icon="pencil",
                    root_button_anim=True,
                    hint_animation=True,
                )
            )
        )


    def callback(self, *args):
        print(args)

Example().run()