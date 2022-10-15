#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# pythonでROSのソフトウェアを記述するときにimportするモジュール
import rospy
import sys
import moveit_commander
import tf
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion, Vector3

# # 実際にpublishする関数
# def publish_date():
#     # 初期化宣言 : このソフトウェアは"pose_planner"という名前
#     rospy.init_node('pose_planner', anonymous=True)

#     # nodeの宣言: publisherのインスタンスを作る
#     # hello_worldというtopicにString型のmessageを送るPublisherを作成
#     oc = rospy.Publisher('hello_world', String, queue_size=100)

#     # 1秒間にpublishする数の設定
#     r = rospy.Rate(1)

#     # 送信するデータxを定義する
#     x = 0

#     # OutputCsv型のmessageのインスタンスを作成
#     oc_msg = String()

#     # ctl + Cで終了しない限りwhileループでpublishし続ける
#     while not rospy.is_shutdown():
#         # データを入力
#         oc_msg.data = "Hello World!!!"

#         print(oc_msg.data)

#         # publishする関数
#         oc.publish(oc_msg)

#         # rだけ待機
#         r.sleep()


def main():
    # MoveitCommanderの初期化
    moveit_commander.roscpp_initialize(sys.argv)

    # ノードの生成
    rospy.init_node("pose_planner")

    # MoveGroupCommanderの準備
    move_group = moveit_commander.MoveGroupCommander("front_left_foot")

    # エンドポイントの姿勢でゴール状態を指定
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position = Vector3(0.33, -0.14, 0)
    q = tf.transformations.quaternion_from_euler(0, 0, 0)
    pose_goal.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    move_group.set_pose_target(pose_goal)

    # モーションプランの計画と実行
    move_group.go(wait=True)

    # 後処理
    move_group.stop()
    move_group.clear_pose_targets()

# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        # publish_date()
        main()

    except rospy.ROSInterruptException: pass