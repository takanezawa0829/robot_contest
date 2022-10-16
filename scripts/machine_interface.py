#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity
from turtle import pos
import rospy
from sensor_msgs.msg import JointState
import HiwonderServoController as servo
import config
servo.setConfig(config.serial_port, config.serial_timeout)
import numpy as np
import math

def deg2data(deg, standard, reverse):
    if(reverse):
        return standard - deg / config.data_rad_diff
    return standard + deg / config.data_rad_diff

def data2deg(data, standard, reverse):
    if(reverse):
        return (standard - data) * config.data_rad_diff
    return (data - standard) * config.data_rad_diff

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    # ここで実際にサーボを動作させる
    position = np.rad2deg(data.position)
    position = np.array(position)
    front_left_foot = [position[0], position[1], position[2]]
    print(front_left_foot)
    front_left_foot = [
        deg2data(front_left_foot[0], 500, True),
        deg2data(front_left_foot[1], 500, True),
        deg2data(front_left_foot[2], 200, False),
    ]
    front_left_foot = np.array(front_left_foot).astype(int)
    servo.moveServo(1, front_left_foot[0], 500)
    servo.moveServo(2, front_left_foot[1], 500)
    servo.moveServo(3, front_left_foot[2], 500)

def serial():
    rospy.init_node('machine_interface', anonymous=True)

    # Subscriberとしてrobot_joint_dataというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('robot_joint_data', JointState, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    serial()