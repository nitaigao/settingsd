from .display import Display

class Layout:
    def __init__(self):
        self.displays = []

    def add_display(self, name, scale, x, y, enabled, primary):
        display = Display(name, scale, x, y, enabled, primary)
        self.displays.append(display)

    def config(self):
        displays = {}
        for el in self.displays:
            displays[el.name] = (el.x, el.y, el.scale, el.enabled, el.primary)
        return displays

    def matches(self, display_names):
        if len(display_names) != len(self.displays):
            return False

        names = list(map(lambda d: d.name, self.displays))
        return set(display_names) == set(names)
