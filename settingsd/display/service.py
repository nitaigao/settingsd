import dbus.service

from .arrangement import Arrangement

class DisplayService(dbus.service.Object):
    @dbus.service.method("org.os.Settings.Display",
                         in_signature='a(sii)', out_signature='a{s(iiibb)}')
    def FindLayout(self, outputs):
        print(outputs)
        arrangement = Arrangement.locate()
        layout = arrangement.find_or_create(outputs)
        return layout.config()
