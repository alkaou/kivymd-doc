from kivy.lang import Builder

from kivymd.app import MDApp

from kivymd.uix.segmentedcontrol import (
    MDSegmentedControl, MDSegmentedControlItem
)


KV = '''
MDScreen:

    MDSegmentedControl:
        pos_hint: {"center_x": .5, "center_y": .5}
        on_active: app.on_active(*args)

        MDSegmentedControlItem:
            text: "Male"

        MDSegmentedControlItem:
            text: "Female"

        MDSegmentedControlItem:
            text: "All"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_active(
        self,
        segmented_control: MDSegmentedControl,
        segmented_item: MDSegmentedControlItem,
    ) -> None:
        '''Called when the segment is activated.'''
        print(segmented_item)


Example().run()