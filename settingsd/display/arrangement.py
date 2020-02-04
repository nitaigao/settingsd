class Arrangement:
    def __init__(self):
        self.layouts = []

    def add_layout(self, layout):
        self.layouts.append(layout)

    def find_layout(self, display_names):
        for layout in self.layouts:
            if layout.matches(display_names):
                return layout