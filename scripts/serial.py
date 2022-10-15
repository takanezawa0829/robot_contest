#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    # ここで実際にサーボを動作させる
    rospy.loginfo(data)

def serial():
    rospy.init_node('serial', anonymous=True)

    # Subscriberとしてjoint_statesというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('joint_states', JointState, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    serial()