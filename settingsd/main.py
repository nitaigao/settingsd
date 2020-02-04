#!/usr/bin/env python

from gi.repository import GLib

import dbus
import dbus.mainloop.glib

from display import DisplayService

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()
    session_bus = dbus.SessionBus()
    
    bus_name = 'org.os.Settings'
    name = dbus.service.BusName(bus_name, session_bus)

    display = DisplayService(session_bus, '/org/os/Settings/Display')
    display.init()

    print(f"settingsd started / {bus_name}")
    loop.run()