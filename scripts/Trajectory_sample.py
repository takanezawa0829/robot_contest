#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# pythonでROSのソフトウェアを記述するときにimportするモジュール
import time
import rospy
# 自分で定義したmessageファイルから生成されたモジュール
from robot_contest.msg import MoveServo
import KinematicsClass as Kinematics
import config
import HiwonderServoController as servo
import numpy as np
import math
servo.setConfig('/dev/ttyUSB0', 2)

# 左か右かを動的に変更する必要がある + 前真ん中後ろも
foot = {
    'left_or_right': 'left',
    'front_or_middle_or_back': 'front',
}
foot_config = config.foot[foot['front_or_middle_or_back']][foot['left_or_right']]

def get_theta(ids):
    # sample = {
    #     1: 100,
    #     2: 200,
    #     3: 100,
    # }
    # return sample
    angle = servo.multServoPosRead(ids)
    print('サーボから取得した値:', angle)
    return angle

def convert_to_rad(data, order):
    rad = math.radians((data - foot_config['servo_basis'][order]) * config.servo['servo_angle'])
    if (foot_config['servo_reverse'][order]):
        rad = rad * -1
    return rad

def convert_to_value(rad, order):
    data = (rad / config.servo['servo_angle'])
    if (foot_config['servo_reverse'][order]):
        data = data * -1
    data = data + foot_config['servo_basis'][order]
    data = int(data)
    return data

# def move_servo(vels, time):
#     for id in vels:
#         servo.moveServo(id, convert_to_value(vels[id] * time, id), time)
#     return


inverse_kinematics = Kinematics.InverseKinematics(foot_config['l_len'], foot['left_or_right'] == 'right')
def callback(data):
    print('recieve data')
    time = data.time
    ids = [
        foot_config['servo_id'][0],
        foot_config['servo_id'][1],
        foot_config['servo_id'][2],
    ]
    ang = get_theta(ids)
    # サーボの返り値から角度に変換する
    ang = np.matrix([
        [convert_to_rad(ang[ids[0]], 0)],
        [convert_to_rad(ang[ids[1]], 1)],
        [convert_to_rad(ang[ids[2]], 2)],
    ])
    # 先端速度を設定
    vel = np.matrix([[data.coordinate_x / time], [data.coordinate_y / time], [data.coordinate_z / time]])
    inverse_kinematics.set_pram(ang, vel)
    ang_vel = inverse_kinematics.get_AVE()

    print('角速度', np.rad2deg(ang_vel))

    # サーボ動作
    for num in range(3):
        # servo.moveServo(ids[num], convert_to_value(ang_vel[num] * time, num), int(time * 1000))
        print('id', ids[num])
        print('位置', convert_to_value(ang_vel[num] * time, num))
        print('time', int(time * 1000))

def main():
    # 初期化宣言 : このソフトウェアは"move_servo"という名前
    rospy.init_node('move_servo', anonymous=True)

    # Subscriberとしてmove_servoというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('move_servo', MoveServo, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        # servo.moveServo(1, 500, 500)
        # servo.moveServo(2, 350, 500)
        # servo.moveServo(3, 600, 500)
        main()

    except rospy.ROSInterruptException: pass