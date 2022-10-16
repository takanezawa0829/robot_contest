#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

from itertools import count
import rospy
from sensor_msgs.msg import JointState
import config

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    config.count += 1
    if config.count == 2:
        # publishする関数
        oc.publish(data)
        config.count = 0

def receive_joint_state():
    rospy.init_node('receive_joint_state', anonymous=True)

    # robot_joint_dataというtopicにJointState型のmessageを送るPublisherを作成
    global oc
    oc = rospy.Publisher('robot_joint_data', JointState, queue_size=100)

    # Subscriberとしてjoint_statesというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('joint_states', JointState, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    receive_joint_state()