from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDSwitch:
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True
        # disabled_color: "lightgrey"
        # disabled: True
        # icon_inactive: "close"
        icon_active: "check"
        # icon_inactive: "close"
        # thumb_color_active: "green"
        # thumb_color_inactive: "brown"
        on_active: app.on_active(*args)

'''


class Test(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_active(self, instance_switch, active_value):
        print(active_value)


Test().run()