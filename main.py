from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class Test(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDBottomNavigation(
                    MDBottomNavigationItem(
                        MDLabel(
                            text='Mail',
                            halign='center',
                        ),
                        name='screen 1',
                        text='Mail',
                        icon='gmail',
                        badge_icon="numeric-10",
                    ),
                    MDBottomNavigationItem(
                        MDLabel(
                            text='Twitter',
                            halign='center',
                        ),
                        name='screen 2',
                        text='Twitter',
                        icon='twitter',
                        badge_icon="numeric-10",
                    ),
                    MDBottomNavigationItem(
                        MDLabel(
                            text='LinkedIN',
                            halign='center',
                        ),
                        name='screen 3',
                        text='LinkedIN',
                        icon='linkedin',
                        badge_icon="numeric-10",
                    ),
                    selected_color_background="orange",
                    text_color_active="lightgrey",
                )
            )
        )


Test().run()