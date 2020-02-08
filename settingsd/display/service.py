import dbus.service

from .display import Display
from .arrangement import Arrangement

class DisplayService(dbus.service.Object):
    @dbus.service.method("org.os.Settings.Display",
                         in_signature='as', out_signature='a{s(iiibb)}')
    def FindLayout(self, names):
        arrangement = Arrangement.from_file('/etc/settingsd/monitors.json')
        layout = arrangement.find_layout(names)
        if layout is None:
            return {}
        result = layout.config()
        print(result)
        return result
