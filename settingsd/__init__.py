from gi.repository import GLib

import dbus
import dbus.mainloop.glib

from settingsd.display.service import DisplayService

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()
    bus = dbus.SystemBus()

    bus_name = 'org.os.Settings'
    name = dbus.service.BusName(bus_name, bus)
    DisplayService(bus, '/org/os/Settings/Display')

    print(f"settingsd started / {bus_name}")
    loop.run()
