import numpy as np
import moveit_commander

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

def quadratic_move(move_group, h, d, i, reverse):
    # ウェイポイント群
    waypoints = []
    scale = 1.0

    # ウェイポイントの追加
    list = quadratic(h, d, i, reverse)
    for i in np.arange(len(list)):
        wpose = move_group.get_current_pose().pose
        # wpose.position.x += scale * 0.07
        wpose.position.z += scale * list[i]['y']
        wpose.position.y += scale * list[i]['x']
        waypoints.append(wpose)

    return waypoints