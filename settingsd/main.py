#!/usr/bin/env python

from gi.repository import GLib

import dbus
import dbus.mainloop.glib

from display import DisplayService

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()
    system_bus = dbus.SystemBus()

    bus_name = 'org.os.Settings'
    name = dbus.service.BusName(bus_name, system_bus)

    display = DisplayService(system_bus, '/org/os/Settings/Display')
    display.init()

    print(f"settingsd started / {bus_name}")
    loop.run()
