#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

import rospy
from sensor_msgs.msg import JointState
import HiwonderServoController as servo
import config
import numpy as np

def deg2data(deg, standard, reverse):
    if(reverse):
        return int(round(standard - deg / config.data_rad_diff))
    return int(round(standard + deg / config.data_rad_diff))

def data2deg(data, standard, reverse):
    if(reverse):
        return (standard - data) * config.data_rad_diff
    return (data - standard) * config.data_rad_diff

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    # ここで実際にサーボを動作させる
    for i in np.arange(len(data.name)):
        # dummy jointを除外
        if data.name[i] in ang_list:
            id = ang_list[data.name[i]]['id']
            standard = ang_list[data.name[i]]['standard']
            reverse = ang_list[data.name[i]]['reverse']
            deg = np.rad2deg(data.position[i])
            # print('joint名', data.name[i])
            # print('id', id)
            # print('角度[deg]', deg)
            # print('standard', standard)
            # print('reverse', reverse)
            ang_data = deg2data(deg, standard, reverse)
            # print('ang_data', ang_data)
            # print('-----------------------')
            # サーボを動作
            servo.moveServo(id, ang_data, 500)

def serial():
    rospy.init_node('machine_interface', anonymous=True)

    global ang_list
    ang_list = {}
    foot = config.foot
    for i in np.arange(3):
        ang_list[foot['front']['left']['rev'][i]] = {
            'id': foot['front']['left']['id'][i],
            'standard': foot['front']['left']['standard'][i],
            'reverse': foot['front']['left']['reverse'][i],
        }
        ang_list[foot['front']['right']['rev'][i]] = {
            'id': foot['front']['right']['id'][i],
            'standard': foot['front']['right']['standard'][i],
            'reverse': foot['front']['right']['reverse'][i],
        }
        ang_list[foot['middle']['left']['rev'][i]] = {
            'id': foot['middle']['left']['id'][i],
            'standard': foot['middle']['left']['standard'][i],
            'reverse': foot['middle']['left']['reverse'][i],
        }
        ang_list[foot['middle']['right']['rev'][i]] = {
            'id': foot['middle']['right']['id'][i],
            'standard': foot['middle']['right']['standard'][i],
            'reverse': foot['middle']['right']['reverse'][i],
        }
        ang_list[foot['end']['left']['rev'][i]] = {
            'id': foot['end']['left']['id'][i],
            'standard': foot['end']['left']['standard'][i],
            'reverse': foot['end']['left']['reverse'][i],
        }
        ang_list[foot['end']['right']['rev'][i]] = {
            'id': foot['end']['right']['id'][i],
            'standard': foot['end']['right']['standard'][i],
            'reverse': foot['end']['right']['reverse'][i],
        }
    
    servo.setConfig(config.serial_port, config.serial_timeout)


    # Subscriberとしてrobot_joint_dataというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('robot_joint_data', JointState, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    serial()