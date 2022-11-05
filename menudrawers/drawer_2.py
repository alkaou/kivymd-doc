from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar


class BaseNavigationDrawerItem(MDNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.text_color = "#4a4939"
        self.icon_color = "#4a4939"
        self.focus_color = "#e7e4c0"


class DrawerLabelItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.focus_behavior = False
        self._no_ripple_effect = True
        self.selected_color = "#4a4939"


class DrawerClickableItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_color = "#c5bdd2"
        self.selected_color = "#0c6c4d"


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
                        MDNavigationDrawerMenu(
                            MDNavigationDrawerHeader(
                                title="Header title",
                                title_color="#4a4939",
                                text="Header text",
                                spacing="4dp",
                                padding=("12dp", 0, 0, "56dp"),
                            ),
                            MDNavigationDrawerLabel(
                                text="Mail",
                            ),
                            DrawerClickableItem(
                                icon="gmail",
                                right_text="+99",
                                text_right_color="#4a4939",
                                text="Inbox",
                            ),
                            DrawerClickableItem(
                                icon="send",
                                text="Outbox",
                            ),
                            MDNavigationDrawerDivider(),
                            MDNavigationDrawerLabel(
                                text="Labels",
                            ),
                            DrawerLabelItem(
                                icon="information-outline",
                                text="Label",
                            ),
                            DrawerLabelItem(
                                icon="information-outline",
                                text="Label",
                            ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    )
                )
            )
        )

    def nav_drawer_open(self, *args):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")


Example().run()