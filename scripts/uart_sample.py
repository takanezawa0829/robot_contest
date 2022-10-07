#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

import serial

use_port = '/dev/ttyUSB0'

_serial = serial.Serial(use_port)
_serial.baudrate = 9600

_serial.parity = serial.PARITY_NONE
_serial.bytesize = serial.EIGHTBITS
_serial.stopbits = serial.STOPBITS_ONE
_serial.timeout = 5

ori_data = "spider_robot!!"

print("送信するデータ", ori_data)

bin = ori_data.encode('utf-8')

_serial.write(bin)

_serial.flush()

return_bin = _serial.readline()

return_data = return_bin.decode('utf-8')

print("帰ってきた値: ", return_data)