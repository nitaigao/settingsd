from .display import Display

class Layout:
    def __init__(self):
        self.displays = []

    def add_display(self, name, scale, x, y):
        display = Display(name, scale, x, y)
        self.displays.append(display)

    def config(self):
        displays = {}
        for el in self.displays:
            displays[el.name] = {'scale': el.scale, 'x': el.x, 'y': el.y}
        return displays

    def matches(self, display_names):
        if len(display_names) != len(self.displays):
            return False
        
        names = list(map(lambda d: d.name, self.displays))
        return set(display_names) == set(names)