#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# output_csvにデータをpublishするサンプルプログラム

# pythonでROSのソフトウェアを記述するときにimportするモジュール
from os import rename
import rospy
# 自分で定義したmessageファイルから生成されたモジュール
from robot_contest.msg import OutputCsv

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


# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        publish_date()

    except rospy.ROSInterruptException: pass