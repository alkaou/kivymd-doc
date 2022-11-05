from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.segmentedcontrol import (
    MDSegmentedControl, MDSegmentedControlItem
)


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                MDSegmentedControl(
                    MDSegmentedControlItem(
                        text="Male"
                    ),
                    MDSegmentedControlItem(
                        text="Female"
                    ),
                    MDSegmentedControlItem(
                        text="All"
                    ),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    # on_active=self.on_active(*args),
                )
            )
        )

    def on_active(
        self,
        segmented_control: MDSegmentedControl,
        segmented_item: MDSegmentedControlItem,
    ) -> None:
        '''Called when the segment is activated.'''
        print(segmented_item)



Example().run()