#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# 機体が命令受付状態になっているときに,MoveCommandを通すためのプログラム

# pythonでROSのソフトウェアを記述するときにimportするモジュール
from os import rename
import rospy
import config
# 自分で定義したmessageファイルから生成されたモジュール
from robot_contest.msg import MoveCommand

def return_flag():
    f = open(config.directory_path + '/scripts/command_stop.txt', 'r')
    data = str(f.read())
    f.close()
    return data

def callback(data):
    if return_flag() == 'False':
        oc.publish(data)
        print('published', data.command, data.speed)


def main():
    rospy.init_node('receive_command', anonymous=True)

    global oc
    oc = rospy.Publisher('command_dummy', MoveCommand, queue_size=100)

    rospy.Subscriber('move_command', MoveCommand, callback)
    # topic更新の待ちうけを行う関数
    rospy.spin()


# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        main()

    except rospy.ROSInterruptException: pass