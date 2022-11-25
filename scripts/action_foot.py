import numpy as np
import moveit_commander
import config

# hが高さ、dが幅、iが解像度、reverseは逆にするか
def quadratic(h, d, i, reverse):
    list = []
    # 1メモリがどのくらいか
    one = d / i
    # a = 1の時の頂点の時のx
    max_x = d / 2
    # a = 1の時の頂点の時のy
    max_y = -max_x * (max_x - d)
    # 高さがhとなるようなaを定義
    a = h / max_y

    if reverse:
        for z in np.arange(i + 1):
            x = -1 * z * one
            data = {
                'x': x,
                'y': -a * x * (x + d),
            }
            list.append(data)
    else:
        for z in np.arange(i + 1):
            x = z * one
            data = {
                'x': x,
                'y': -a * x * (x - d),
            }
            list.append(data)

    return list

# 2次関数
def quadratic_move(move_group, h, d, i, reverse, z_theta = 0):
    # ウェイポイント群
    waypoints = []
    scale = 1.0

    z_rad = np.deg2rad(z_theta)
    # 回転行列を定義
    z_rev = np.matrix([
        [np.cos(z_rad), -np.sin(z_rad), 0],
        [np.sin(z_rad), np.cos(z_rad), 0],
        [0, 0, 1],
    ])

    # ウェイポイントの追加
    list = quadratic(h, d, i, reverse)
    for i in np.arange(len(list)):
        wpose = move_group.get_current_pose().pose
        waypoint = np.matrix([
            [scale * list[i]['x']],
            [0],
            [scale * list[i]['y']],
        ])
        waypoint = np.dot(z_rev, waypoint)
        print(waypoint)
        wpose.position.x += waypoint[0, 0]
        wpose.position.y += waypoint[1, 0]
        wpose.position.z += waypoint[2, 0]
        waypoints.append(wpose)

    return waypoints

# 初期姿勢
def init_pose():
    front_left_foot = moveit_commander.MoveGroupCommander("front_left_foot")
    front_right_foot = moveit_commander.MoveGroupCommander("front_right_foot")
    middle_left_foot = moveit_commander.MoveGroupCommander("middle_left_foot")
    middle_right_foot = moveit_commander.MoveGroupCommander("middle_right_foot")
    end_left_foot = moveit_commander.MoveGroupCommander("end_left_foot")
    end_right_foot = moveit_commander.MoveGroupCommander("end_right_foot")
    # 関節の角度でゴール状態を指定
    init_ang = [np.deg2rad(0), np.deg2rad(-10), np.deg2rad(90)]
    joint_goal = {
        'front_left_foot': {
            config.foot['front']['left']['rev'][0]: init_ang[0],
            config.foot['front']['left']['rev'][1]: init_ang[1],
            config.foot['front']['left']['rev'][2]: init_ang[2],
        },
        'front_right_foot': {
            config.foot['front']['right']['rev'][0]: init_ang[0],
            config.foot['front']['right']['rev'][1]: -1 * init_ang[1],
            config.foot['front']['right']['rev'][2]: -1 * init_ang[2],
        },
        'middle_left_foot': {
            config.foot['middle']['left']['rev'][0]: init_ang[0],
            config.foot['middle']['left']['rev'][1]: init_ang[1],
            config.foot['middle']['left']['rev'][2]: init_ang[2],
        },
        'middle_right_foot': {
            config.foot['middle']['right']['rev'][0]: init_ang[0],
            config.foot['middle']['right']['rev'][1]: -1 * init_ang[1],
            config.foot['middle']['right']['rev'][2]: -1 * init_ang[2],
        },
        'end_left_foot': {
            config.foot['end']['left']['rev'][0]: init_ang[0],
            config.foot['end']['left']['rev'][1]: init_ang[1],
            config.foot['end']['left']['rev'][2]: init_ang[2],
        },
        'end_right_foot': {
            config.foot['end']['right']['rev'][0]: init_ang[0],
            config.foot['end']['right']['rev'][1]: -1 * init_ang[1],
            config.foot['end']['right']['rev'][2]: -1 * init_ang[2],
        },
    }
    # 角度を設定
    front_left_foot.set_joint_value_target(joint_goal['front_left_foot'])
    # モーションプランの計画と実行
    front_left_foot.go(wait=True)
    # 後処理
    front_left_foot.stop()

    # 角度を設定
    front_right_foot.set_joint_value_target(joint_goal['front_right_foot'])
    # モーションプランの計画と実行
    front_right_foot.go(wait=True)
    # 後処理
    front_right_foot.stop()

    # 角度を設定
    middle_left_foot.set_joint_value_target(joint_goal['middle_left_foot'])
    # モーションプランの計画と実行
    middle_left_foot.go(wait=True)
    # 後処理
    middle_left_foot.stop()

    # 角度を設定
    middle_right_foot.set_joint_value_target(joint_goal['middle_right_foot'])
    # モーションプランの計画と実行
    middle_right_foot.go(wait=True)
    # 後処理
    middle_right_foot.stop()

    # 角度を設定
    end_left_foot.set_joint_value_target(joint_goal['end_left_foot'])
    # モーションプランの計画と実行
    end_left_foot.go(wait=True)
    # 後処理
    end_left_foot.stop()

    # 角度を設定
    end_right_foot.set_joint_value_target(joint_goal['end_right_foot'])
    # モーションプランの計画と実行
    end_right_foot.go(wait=True)
    # 後処理
    end_right_foot.stop()

# 直線移動
def linear_move(move_group, x, y, z):
    # ウェイポイント群
    waypoints = []
    scale = 1.0

    # ウェイポイントの追加
    wpose = move_group.get_current_pose().pose
    wpose.position.x += scale * x
    wpose.position.y += scale * y
    wpose.position.z += scale * z
    waypoints.append(wpose)

    return waypoints
