import dbus.service
from json import dumps

from display import Arrangement, Display, Layout

class DisplayService(dbus.service.Object):
    def init(self):
        self.arrangement = Arrangement()

        layoutA = Layout()
        layoutA.add_display("laptop", 3, 0, 1200)
        self.arrangement.add_layout(layoutA)
            
        layoutB = Layout()
        layoutB.add_display("LG", 2, 0, 0)
        layoutB.add_display("laptop", 3, 0, 1200)
        self.arrangement.add_layout(layoutB)

    @dbus.service.method("org.os.SettingsDaemon.Display",
                         in_signature='as', out_signature='s')
    def Arrangement(self, args):
        names = args
        layout = self.arrangement.find_layout(names)
        return dumps(layout.config())  