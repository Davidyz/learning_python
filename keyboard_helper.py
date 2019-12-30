#!/usr/bin/python3.6
import os, time
"""
Automatically disable the integrated keyboard when the external keyboard is plugged. The code is keyboard-specific, ie. when you use another external keyboard you need to modify the code.
"""
keyboard = "usb-AKKO_AKKO_3068BT-event-kbd"

while True:
    if keyboard in os.listdir("/dev/input/by-id/"):
        os.system('xinput set-int-prop 12 "Device Enabled" 8 0')
    else:
        os.system('xinput set-int-prop 12 "Device Enabled" 8 1')
    time.sleep(1)
