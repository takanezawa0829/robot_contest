#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# output_csvにデータをpublishするサンプルプログラム

import rospy
# 自分で定義したmessageファイルから生成されたモジュール
from robot_contest.msg import OutputCsv
# pythonでROSのソフトウェアを記述するときにimportするモジュール
from sensor_msgs.msg import JointState
import config
import numpy as np

# 実際にpublishする関数
def publish_date():
    # 初期化宣言 : このソフトウェアは"publish_date"という名前
    rospy.init_node('publish_date', anonymous=True)

    # nodeの宣言: publisherのインスタンスを作る
    # output_csvというtopicにOutputCsv型のmessageを送るPublisherを作成
    oc = rospy.Publisher('output_csv', OutputCsv, queue_size=100)

    # 1秒間にpublishする数の設定
    r = rospy.Rate(10)

    # 送信するデータxを定義する
    x = 0

    # OutputCsv型のmessageのインスタンスを作成
    oc_msg = OutputCsv()

    # ヘッダーを設定
    oc_msg.header = ["項目1", "項目2", "項目3", "項目4", "項目5"]

    # ctl + Cで終了しない限りwhileループでpublishし続ける
    while not rospy.is_shutdown():
        # データを入力
        oc_msg.value = []
        for i in range(5):
            oc_msg.value.append(x)
            x += 1

        print(oc_msg.value)

        # publishする関数
        oc.publish(oc_msg)

        # rだけ待機
        r.sleep()

def callback(data):
    joint_list = {}
    foot = config.foot
    for i in np.arange(3):
        joint_list[foot['front']['left']['rev'][i]] = 0
        joint_list[foot['front']['right']['rev'][i]] = 0
        joint_list[foot['middle']['left']['rev'][i]] = 0
        joint_list[foot['middle']['right']['rev'][i]] = 0
        joint_list[foot['end']['left']['rev'][i]] = 0
        joint_list[foot['end']['right']['rev'][i]] = 0

    for i in np.arange(len(data.name)):
        if data.name[i] in joint_list:
            joint_list[data.name[i]] = np.rad2deg(data.position[i])

    # OutputCsv型のmessageのインスタンスを作成
    oc_msg = OutputCsv()

    # ヘッダーを設定
    oc_msg.header = foot['front']['left']['rev']

    oc_msg.value = []
    for i in np.arange(len(oc_msg.header)):
        oc_msg.value.append(joint_list[oc_msg.header[i]])

    # publishする関数
    oc.publish(oc_msg)

def main():
    rospy.init_node('foot_action_stock', anonymous=True)

    # output_csvというtopicにOutputCsv型のmessageを送るPublisherを作成
    global oc
    oc = rospy.Publisher('output_csv', OutputCsv, queue_size=100)

    # Subscriberとしてrobot_joint_dataというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('robot_joint_data', JointState, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()

    return


# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        main()

    except rospy.ROSInterruptException: pass