from os import path
from json import load, dump

from .layout import Layout

class Arrangement:
    def __init__(self, file_path='/etc/settingsd/monitors.json'):
        self.file_path = file_path
        self.layouts = []

    @staticmethod
    def locate():
        arrangement = Arrangement()
        arrangement.load()
        return arrangement

    def load(self):
        if not path.exists(self.file_path):
            with open(self.file_path, 'w+') as file:
                dump([], file)
        with open(self.file_path, 'r') as file:
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
                self.add_layout(layout)

    def save(self):
        with open(self.file_path, 'w') as file:
            arrangment_data = []
            for layout in self.layouts:
                layout_data = []
                for display in layout.displays:
                    layout_data.append({
                        "name": display.name,
                        "x": display.x,
                        "y": display.y,
                        "scale": display.scale,
                        "enabled": display.enabled,
                        "primary": display.primary
                    })
                arrangment_data.append(layout_data)
            dump(arrangment_data, file, indent=2)

    def config(self):
        layouts = []
        for layout in self.layouts:
            layouts.append(layout.config())
        return layouts

    def add_layout(self, layout):
        self.layouts.append(layout)

    def find_layout(self, displays):
        names = list(map(lambda d: d[0], displays))
        for layout in self.layouts:
            if layout.matches(names):
                return layout

    def create_layout(self, displays):
        layout = Layout()
        x_position = 0
        primary = True
        for display in displays:
            layout.add_display(display[0], 1, x_position, 0, True, primary)
            primary = False
            x_position += display[1]
        return layout

    def find_or_create(self, displays):
        layout = self.find_layout(displays)
        if layout is not None:
            return layout

        new_layout = self.create_layout(displays)
        self.add_layout(new_layout)
        self.save()
        return new_layout
