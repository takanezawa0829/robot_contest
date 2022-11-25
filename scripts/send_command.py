#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# output_csvにデータをpublishするサンプルプログラム

# pythonでROSのソフトウェアを記述するときにimportするモジュール
from os import rename
import rospy
import config
# 自分で定義したmessageファイルから生成されたモジュール
from std_msgs.msg import String
from robot_contest.msg import MoveCommand

# 実際にpublishする関数
def publish_date():
    # 初期化宣言 : このソフトウェアは"hello_world"という名前
    rospy.init_node('send_command', anonymous=True)

    # nodeの宣言: publisherのインスタンスを作る
    # hello_worldというtopicにMoveCommand型のmessageを送るPublisherを作成
    oc = rospy.Publisher('move_command', MoveCommand, queue_size=100)

    # 1秒間にpublishする数の設定
    r = rospy.Rate(5)

    # 送信するデータxを定義する
    x = 0

    # OutputCsv型のmessageのインスタンスを作成
    oc_msg = MoveCommand()

    # ctl + Cで終了しない限りwhileループでpublishし続ける
    while not rospy.is_shutdown():

        # データを入力
        oc_msg.command = "前進"
        oc_msg.speed = 10

        print(oc_msg.command, oc_msg.speed)

        # publishする関数
        oc.publish(oc_msg)

        # rだけ待機
        r.sleep()


# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        publish_date()

    except rospy.ROSInterruptException: pass
