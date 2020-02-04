#!/usr/bin/env python

from gi.repository import GLib

import dbus
import gobject
import dbus.service
import dbus.mainloop.glib
from json import dumps

from display import Arrangement, Display, Layout

class ArrangementService(dbus.service.Object):
    @dbus.service.method("org.os.SettingsDaemon.Display",
                         in_signature='as', out_signature='s')
    def Arrangement(self, args):
        names = args
        layout = self.arrangement.find_layout(names)
        return dumps(layout.config())  

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    arrangement = Arrangement()

    layoutA = Layout()
    layoutA.add_display("laptop", 3, 0, 1200)
    arrangement.add_layout(layoutA)
        
    layoutB = Layout()
    layoutB.add_display("LG", 2, 0, 0)
    layoutB.add_display("laptop", 3, 0, 1200)
    arrangement.add_layout(layoutB)

    session_bus = dbus.SessionBus()
    bus_name = 'org.os.SettingsDaemon'
    name = dbus.service.BusName(bus_name, session_bus)
    service = ArrangementService(session_bus, '/org/os/SettingsDaemon/Display')
    service.arrangement = arrangement

    print(f"settingd started at {bus_name}")
    loop.run()