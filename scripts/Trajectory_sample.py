#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# pythonでROSのソフトウェアを記述するときにimportするモジュール
import rospy
# 自分で定義したmessageファイルから生成されたモジュール
from robot_contest.msg import MoveServo
import KinematicsClass as Kinematics
import config
import HiwonderServoController as _servo
import numpy as np

def get_theta(ids):
    sample = {
        1: 100,
        2: 200,
        3: 100,
    }
    return sample
    angle = _servo.multServoPosRead(ids)
    print(angle)
    return angle

def move_servo(ang_vels, time):
    for ang_vel in ang_vels:
        print(ang_vel)

inverse_kinematics = Kinematics.InverseKinematics(config.l_len, False)
def callback(data):
    print('recieve data')
    time = data.time
    vel = np.matrix([[data.coordinate_x / time], [data.coordinate_y / time], [data.coordinate_z / time]])
    # IDの設定に関しては動的にする必要がある
    # 足のnum
    foot_num = 0
    ids = [
        3 * foot_num + 1, # 第一関節
        3 * foot_num + 2, # 第二関節
        3 * foot_num + 3, # 第三関節
    ]
    ang = get_theta(ids)
    ang = np.matrix([
        [ang[ids[0]]],
        [ang[ids[1]]],
        [ang[ids[2]]],
    ])
    inverse_kinematics.set_pram(ang, vel)
    ang_vel = inverse_kinematics.get_AVE()
    ang_vel_list = {}
    ang_vel_list[ids[0]] = ang_vel[0]
    ang_vel_list[ids[1]] = ang_vel[1]
    ang_vel_list[ids[2]] = ang_vel[2]
    print(ang_vel_list)
    move_servo(ang_vel_list, time)
    return

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
        main()

    except rospy.ROSInterruptException: pass