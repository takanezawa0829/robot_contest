#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# 全脚0度から機体を初期姿勢に移動するプログラム

# pythonでROSのソフトウェアを記述するときにimportするモジュール
import rospy
import sys
import moveit_commander
from geometry_msgs.msg import Quaternion, Vector3
import action_foot

def main():
    # ノードの生成
    rospy.init_node("pose_planner")

    # 初期姿勢に移動
    action_foot.init_pose()

# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        # MoveitCommanderの初期化
        moveit_commander.roscpp_initialize(sys.argv)

        # publish_date()
        main()

    except rospy.ROSInterruptException: pass
