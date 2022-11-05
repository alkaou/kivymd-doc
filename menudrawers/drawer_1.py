from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar


class ContentNavigationDrawer(MDBoxLayout):
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return(
            MDScreen(
                MDNavigationLayout(
                    MDScreenManager(
                        MDScreen(
                            MDTopAppBar(
                                title="Navigation Drawer",
                                elevation=4,
                                pos_hint={"top": 1},
                                md_bg_color="#e7e4c0",
                                specific_text_color="#4a4939",
                                left_action_items=[
                                    ['menu', lambda x: self.nav_drawer_open()]
                                ],
                            )

                        )
                    ),
                    MDNavigationDrawer(
                        ContentNavigationDrawer(),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    ),
                ),
            ),
        )

    def nav_drawer_open(self, *args):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")


Example().run()