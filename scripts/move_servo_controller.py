#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

import rospy
from sensor_msgs.msg import JointState
from robot_contest.msg import MoveCommand
import HiwonderServoController as servo
import config
import numpy as np
import csv

class csv_tool:
    def __init__(self, file_name):
        print('make csv_tool')
        self.__csv_file = open( config.directory_path + "/action_csv/" + file_name, "r", encoding="ms932")
        self.__data = csv.DictReader(self.__csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    def confirm(self):
        return self.__data

    def close_file(self):
        self.__csv_file.close()

def deg2data(deg, standard, reverse):
    if(reverse):
        return int(round(standard - deg / config.data_rad_diff))
    return int(round(standard + deg / config.data_rad_diff))

def data2deg(data, standard, reverse):
    if(reverse):
        return (standard - data) * config.data_rad_diff
    return (data - standard) * config.data_rad_diff

def publish_joint_states(joint_list):
    oc_msg = JointState()
    oc_msg.name = []
    oc_msg.position = []
    oc_msg.velocity = []
    for name in joint_list:
        oc_msg.name.append(name)
        oc_msg.position.append(np.deg2rad(float(joint_list[name])))
        oc_msg.velocity.append(1)
    for i in np.arange(18):
        oc_msg.name.append('d_rev' + str(i + 1))
        oc_msg.position.append(0)
        oc_msg.velocity.append(1)
    oc_msg.header.stamp = rospy.Time.now()
    oc.publish(oc_msg)

def start_stop_publish(bool):
    f = open(config.directory_path + '/scripts/command_stop.txt', 'w')
    f.write(str(bool))
    f.close()

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    if data.command == 'init_pose':
        # publishを一時停止
        start_stop_publish(True)

        csv_data = csv_tool('init.csv')
        f = csv_data.confirm()
        for row in f:
            for joint_name in row:
                # print('---------')
                # print('ang_list[joint_name]:', ang_list[joint_name])
                # print('row', row)
                # print('row[joint_name]:', row[joint_name])
                ang_data = deg2data(float(row[joint_name]), ang_list[joint_name]['standard'], ang_list[joint_name]['reverse'])
                # print('ang_data:', ang_data)
                
                # rvizに反映
                publish_joint_states(row)

                # サーボを動作
                # servo.moveServo(ang_list[joint_name]['id'], ang_data, 500)

            rospy.sleep(0.1 / data.speed)
                
        csv_data.close_file()
        # publishを再開
        start_stop_publish(False)


def main():
    rospy.init_node('move_servo_controller', anonymous=True)

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
    
    # servo.setConfig(config.serial_port, config.serial_timeout)

    # joint_statesというtopicにJointState型のmessageを送るPublisherを作成
    global oc
    oc = rospy.Publisher('joint_states', JointState, queue_size=100)

    # Subscriberとしてmove_commandというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('move_command', MoveCommand, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    main()