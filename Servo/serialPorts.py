import itertools
import os
import serial.tools.list_ports

if os.name == 'nt':
    import winreg


    def enumerate_serial_ports():
        """ Uses the Win32 registry to return an
            iterator of serial (COM) ports
            existing on this computer.
        """
        path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        except WindowsError:
            #raise IterationError
            pass
        for i in itertools.count():
            try:
                val = winreg.EnumValue(key, i)
                yield str(val[1])
            except EnvironmentError:
                break


    import re


    def full_port_name(portname):
        """ Given a port-name (of the form COM7,
            COM12, CNCA0, etc.) returns a full
            name suitable for opening with the
            Serial class.
        """
        m = re.match('^COM(\d+)$', portname)
        if m and int(m.group(1)) < 10:
            return portname
        return '\\\\.\\' + portname


    def serialPortList():
        return [full_port_name(port) for port in list(enumerate_serial_ports())]
else:
    def serialPortList():
        return [port[0] for port in list(serial.tools.list_ports.comports())]

