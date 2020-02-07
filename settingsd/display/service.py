import dbus.service

from display import Arrangement, Layout

class DisplayService(dbus.service.Object):
    def init(self):
        self.arrangement = Arrangement()

        layout_c = Layout()
        layout_c.add_display("The X.Org Foundation", 2, 0, 0, True, True)
        self.arrangement.add_layout(layout_c)

        layout_a = Layout()
        layout_a.add_display("Sharp Corporation", 3, 0, 0, True, True)
        self.arrangement.add_layout(layout_a)

        layout_b = Layout()
        layout_b.add_display("Goldstar Company Ltd", 2, 0, 0, True, True)
        layout_b.add_display("Sharp Corporation", 3, 320, 1080, True, False)
        self.arrangement.add_layout(layout_b)

    @dbus.service.method("org.os.Settings.Display",
                         in_signature='as', out_signature='a{s(iiibb)}')
    def FindLayout(self, args):
        names = args
        layout = self.arrangement.find_layout(names)
        if layout is None:
            return {}
        result = layout.config()
        print(result)
        return result
