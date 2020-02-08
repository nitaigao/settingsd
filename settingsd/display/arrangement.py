from os import path
from json import load

from .layout import Layout

class Arrangement:
    @staticmethod
    def from_file(file_path):
        arrangement = Arrangement()
        if not path.exists(file_path):
            return arrangement
        with open(file_path, 'r') as file:
            layouts = load(file)
            for layout_data in layouts:
                layout = Layout()
                for display_data in layout_data:
                    layout.add_display(
                        display_data['name'],
                        display_data['scale'],
                        display_data['x'],
                        display_data['y'],
                        display_data['enabled'],
                        display_data['primary'])
                arrangement.add_layout(layout)

        return arrangement

    def __init__(self):
        self.layouts = []

    def add_layout(self, layout):
        self.layouts.append(layout)

    def find_layout(self, display_names):
        for layout in self.layouts:
            if layout.matches(display_names):
                return layout
