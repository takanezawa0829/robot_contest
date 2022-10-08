#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

import serial

use_port = '/dev/ttyUSB0'

CMD_SERVO_MOVE = 0x03
CMD_GET_BATTERY_VOLTAGE = 0x0f
CMD_MULT_SERVO_POS_READ = 0x15

_serial = serial.Serial(use_port)
_serial.baudrate = 9600
_serial.parity = serial.PARITY_NONE
_serial.bytesize = serial.EIGHTBITS
_serial.stopbits = serial.STOPBITS_ONE
_serial.timeout = 5

# サーボの動作（id: int, position: int, time: int）
def MoveServo(id=None,position=None,time=None):
    buf = bytearray(b'\x55\x55')
    buf.append(8)
    buf.append(CMD_SERVO_MOVE)
    # parameters
    buf.append(1)
    buf.extend([(0xff & time), (0xff & (time >> 8))])
    buf.append(id)
    buf.extend([(0xff & position), (0xff & (position >> 8))])
    _serial.write(buf)

# 電圧を取得する
def GetBatteryVoltage():
    buf = bytearray(b'\x55\x55')
    buf.append(2)
    buf.append(CMD_GET_BATTERY_VOLTAGE)
    _serial.write(buf)
    _serial.flush()
    result = _serial.readline()
    a = result[4] | result[5] << 8
    return a

# 現在のサーボの角度を取得する（ids: array[id_1, id_2, ... , id_n]）
def MultServoPosRead(ids):
    buf = bytearray(b'\x55\x55')
    # 取得したいサーボの数+3
    buf.append(6)
    buf.append(CMD_MULT_SERVO_POS_READ)
    buf.append(3)
    for id in ids:
        buf.append(id)
    _serial.write(buf)
    _serial.flush()
    result = _serial.readline()

    # data = []
    # for num in range(len(ids)):
    #     data_one = {
    #         'id': None,
    #         'position': None,
    #     }
    #     i = 3 * num
    #     data_one['id'] = result[5 + i]
    #     data_one['position'] = result[5 + i + 1] | result[5 + i + 2] << 8
    #     data.append(data_one)

    data = {}
    for num in range(len(ids)):
        i = 3 * num
        data[result[5 + i]] = result[5 + i + 1] | result[5 + i + 2] << 8

    return data

# ここからテスト

MoveServo(1,500,500)
MoveServo(2,200,500)
MoveServo(3,900,500)
# print(GetBatteryVoltage())
ids = [1, 2, 3]
print(MultServoPosRead(ids))