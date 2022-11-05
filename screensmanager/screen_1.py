from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreenManager:

    MDScreen:
        name: "screen A"
        md_bg_color: "lightblue"

        MDHeroFrom:
            id: hero_kivymd
            tag: "kivymd"
            size_hint: None, None
            size: "200dp", "200dp"
            pos_hint: {"top": .98}
            x: 24

            FitImage:
                source: "kivymd/images/logo/kivymd-icon-512.png"
                size_hint: None, None
                size: hero_kivymd.size

        MDHeroFrom:
            id: hero_kivy
            tag: "kivy"
            size_hint: None, None
            size: "200dp", "200dp"
            pos_hint: {"top": .98}
            x: 324

            FitImage:
                source: "data/logo/kivy-icon-512.png"
                size_hint: None, None
                size: hero_kivy.size

        MDRaisedButton:
            text: "Move Hero To Screen B"
            pos_hint: {"center_x": .5}
            y: "36dp"
            on_release:
                root.current_heroes = ["kivymd", "kivy"]
                root.current = "screen B"

    MDScreen:
        name: "screen B"
        heroes_to: hero_to_kivymd, hero_to_kivy
        md_bg_color: "cadetblue"

        MDHeroTo:
            id: hero_to_kivy
            tag: "kivy"
            size_hint: None, None
            pos_hint: {"center_x": .5, "center_y": .5}

        MDHeroTo:
            id: hero_to_kivymd
            tag: "kivymd"
            size_hint: None, None
            pos_hint: {"right": 1, "top": 1}

        MDRaisedButton:
            text: "Move Hero To Screen A"
            pos_hint: {"center_x": .5}
            y: "36dp"
            on_release:
                root.current_heroes = ["kivy", "kivymd"]
                root.current = "screen A"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()