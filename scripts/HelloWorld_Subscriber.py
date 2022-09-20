#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy
from std_msgs.msg import String

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    rospy.loginfo(data.data)

def hello_world():
    rospy.init_node('hello_world_sbscriber', anonymous=True)

    # Subscriberとしてhello_worldというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('hello_world', String, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    hello_world()


