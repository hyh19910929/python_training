# -*- coding: utf-8 -*-
import sys
import os
import wmi

print(sys.version)
c = wmi.WMI()
disk = c.Win32_LogicalDisk()[0]
free_space = disk.freeSpace
print(free_space)
