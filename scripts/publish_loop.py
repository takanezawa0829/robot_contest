#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# publishし続けるサンプルプログラム

# pythonでROSのソフトウェアを記述するときにimportするモジュール
from os import rename
import rospy
# 自分で定義したmessageファイルから生成されたモジュール
from robot_contest.msg import MoveServo

# 実際にpublishする関数
def publish_data():
    # 初期化宣言 : このソフトウェアは"publish_loop"という名前
    rospy.init_node('publish_loop', anonymous=True)

    # nodeの宣言: publisherのインスタンスを作る
    # move_servoというtopicにMoveServo型のmessageを送るPublisherを作成
    oc = rospy.Publisher('move_servo', MoveServo, queue_size=100)

    # 1秒間にpublishする数の設定
    r = rospy.Rate(1)

    # messageのインスタンスを作成
    data = MoveServo()

    data.coordinate_x = 12
    data.coordinate_y = 10
    data.coordinate_z = 1
    data.id = 1
    data.time = 10

    # ctl + Cで終了しない限りwhileループでpublishし続ける
    while not rospy.is_shutdown():
        # publishする関数
        oc.publish(data)

        # rだけ待機
        r.sleep()


# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        publish_data()

    except rospy.ROSInterruptException: pass