#!/usr/bin/env python

from gi.repository import GLib

import dbus
import dbus.mainloop.glib

from display.service import DisplayService

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()
    bus = dbus.SystemBus()

    bus_name = 'org.os.Settings'
    name = dbus.service.BusName(bus_name, bus)
    DisplayService(bus, '/org/os/Settings/Display')

    print(f"settingsd started / {bus_name}")
    loop.run()
