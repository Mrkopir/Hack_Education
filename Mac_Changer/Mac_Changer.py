#!/usr/bin/env python

import subprocess

from Parcer import Parcer

class Mac_Changer:
    def __init__(self, interface):
        self.interface = interface

    def mac_changer(self):
        new_mac = subprocess.check_output(f"sudo macchanger -r {self.interface}", shell=True)
        new_mac_list = new_mac.split()
        print(f"You changed your MAC on ({new_mac_list[12]})")

options = Parcer().parce()
mac = Mac_Changer(options.interface)
mac.mac_changer()
