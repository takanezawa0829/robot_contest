#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

# 2次関数によって動作するプログラム

import rospy
import sys
import moveit_commander
import tf
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion, Vector3
import action_foot

def main():
    # ノードの生成
    rospy.init_node("pose_planner")

    # 初期姿勢に移動
    # action_foot.init_pose()

    front_left_waypoints = action_foot.quadratic_move(front_left_foot, 0.08, -0.01, 10, False)
    front_right_waypoints = action_foot.quadratic_move(front_right_foot, 0.08, -0.01, 10, False)
    middle_left_waypoints = action_foot.quadratic_move(middle_left_foot, 0.08, -0.01, 10, False)
    middle_right_waypoints = action_foot.quadratic_move(middle_right_foot, 0.08, -0.01, 10, False)
    end_left_waypoints = action_foot.quadratic_move(end_left_foot, 0.08, -0.01, 10, False)
    end_right_waypoints = action_foot.quadratic_move(end_right_foot, 0.08, -0.01, 10, False)

    ( front_left_plan, front_left_fraction ) = front_left_foot.compute_cartesian_path( front_left_waypoints, 0.01, 0.0)
    ( front_right_plan, front_right_fraction ) = front_right_foot.compute_cartesian_path( front_right_waypoints, 0.01, 0.0)
    ( middle_left_plan, front_left_fraction ) = middle_left_foot.compute_cartesian_path( middle_left_waypoints, 0.01, 0.0)
    ( middle_right_plan, front_right_fraction ) = middle_right_foot.compute_cartesian_path( middle_right_waypoints, 0.01, 0.0)
    ( end_left_plan, front_left_fraction ) = end_left_foot.compute_cartesian_path( end_left_waypoints, 0.01, 0.0)
    ( end_right_plan, front_right_fraction ) = end_right_foot.compute_cartesian_path( end_right_waypoints, 0.01, 0.0)

    front_left_foot.execute( front_left_plan )
    front_right_foot.execute( front_right_plan )
    front_left_foot.execute( middle_left_plan )
    front_right_foot.execute( middle_right_plan )
    front_left_foot.execute( end_left_plan )
    front_right_foot.execute( end_right_plan )


# コマンドプロンプトから呼び出された時だけ関数を実行するためのif文
if __name__ == '__main__':
    try:
        # MoveitCommanderの初期化
        moveit_commander.roscpp_initialize(sys.argv)

        # MoveGroupCommanderの準備
        global front_left_foot, front_right_foot, middle_left_foot, middle_right_foot, end_left_foot, end_right_foot
        front_left_foot = moveit_commander.MoveGroupCommander("front_left_foot")
        front_right_foot = moveit_commander.MoveGroupCommander("front_right_foot")
        middle_left_foot = moveit_commander.MoveGroupCommander("middle_left_foot")
        middle_right_foot = moveit_commander.MoveGroupCommander("middle_right_foot")
        end_left_foot = moveit_commander.MoveGroupCommander("end_left_foot")
        end_right_foot = moveit_commander.MoveGroupCommander("end_right_foot")

        # publish_date()
        main()

    except rospy.ROSInterruptException: pass
