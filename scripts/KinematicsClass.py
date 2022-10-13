#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity

from ast import If
from time import thread_time_ns
import numpy as np
import config

# 順運動学解を求めるためのクラス
class ForwardKinematics:
    def __init__(self, link, foot_link, is_right_side):
        # リンクの長さを定義
        self.link = link
        # ロボット座標系から脚のマニピュレータの付け根までの位置ベクトルを定義
        self.foot_link = foot_link
        # クモ型ロボットの右側のマニピュレータかどうか
        self.is_right_side = is_right_side

    # パラメータを設定
    def set_pram(self, theta):
        self.theta = theta

    # ロボット座標系の順運動学解を計算
    def get_T(self):
        l = self.link
        t = self.theta.flatten().tolist()[0]

        # 脚のマニピュレータの順運動学解を定義
        if self.is_right_side:
            self.T = np.matrix([
                [-1 * np.sin(t[0]) * (l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2]))],
                [np.cos(t[0]) * (l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2]))],
                [l[1] * np.sin(t[1]) + l[2] * np.sin(t[1] + t[2])],
            ])
        else:
            self.T = np.matrix([
                [-1 * np.sin(t[0]) * (l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2]))],
                [-1 * np.cos(t[0]) * (l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2]))],
                [l[1] * np.sin(t[1]) + l[2] * np.sin(t[1] + t[2])],
            ])
        return self.T + self.foot_link

# 逆運動学解を求めるためのクラス
class InverseKinematics:
    def __init__(self, link, is_right_side):
        # リンクの長さを定義
        self.link = link
        # クモ型ロボットの右側のマニピュレータかどうか
        self.is_right_side = is_right_side

    # パラメータを設定
    def set_pram(self, theta, velocity):
        self.theta = theta
        self.velocity = velocity
        # 逆ヤコビアンを定義
        l = self.link
        t = self.theta.flatten().tolist()[0]
        if self.is_right_side:
            self.RJ = np.matrix([
                [(-1 * np.cos(t[0]))/(l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])), (-1 * np.sin(t[0]))/(l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])), 0],
                [(-1 * np.sin(t[0]) * np.cos(t[1] + t[2]))/(l[1] * np.sin(t[2])), (np.cos(t[0]) * np.cos(t[1] + t[2]))/(l[1] * np.sin(t[2])), (np.sin(t[1] + t[2]))/(l[1] * np.sin(t[2]))],
                [(np.sin(t[0]) * (l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])))/(l[1] * l[2] * np.sin(t[2])), (-1 * np.cos(t[0]) * (l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])))/(l[1] * l[2] * np.sin(t[2])), (-1 * (l[1] * np.sin(t[1]) + l[2] * np.sin(t[1] + t[2])))/(l[1] * l[2] * np.sin(t[2]))],
            ])
        else:
            self.RJ = np.matrix([
                [(-1 * np.cos(t[0]))/(l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])), np.sin(t[0])/(l[0] + l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])), 0],
                [(-1 * np.sin(t[0]) * np.cos(t[1] + t[2]))/(l[1] * np.sin(t[2])), (-1 * np.cos(t[0]) * np.cos(t[1] + t[2]))/(l[1] * np.sin(t[2])), (np.sin(t[1] + t[2]))/(l[1] * np.sin(t[2]))],
                [(np.sin(t[0]) * (l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])))/(l[1] * l[2] * np.sin(t[2])), (np.cos(t[0]) * (l[1] * np.cos(t[1]) + l[2] * np.cos(t[1] + t[2])))/(l[1] * l[2] * np.sin(t[2])), (-1 * (l[1] * np.sin(t[1]) + l[2] * np.sin(t[1] + t[2])))/(l[1] * l[2] * np.sin(t[2]))],
            ])

    # 逆ヤコビアンから角速度を求める
    def get_AVE(self):
        return np.dot(self.RJ, self.velocity)

# theta_a = np.matrix([
#     [0],
#     [0],
#     [np.pi / 2],
# ])

# foot_link = np.matrix([
#     [100],
#     [-100],
#     [0],
# ])

# a = ForwardKinematics(config.l_len, foot_link, False)
# a.set_pram(theta_a)
# print(a.get_T())

# theta_b = np.matrix([
#     [90],
#     [45],
#     [-90],
# ])

# velocity_b = np.matrix([
#     [3],
#     [2],
#     [5],
# ])

# b = InverseKinematics(config.l_len, False)
# b.set_pram(theta_b, velocity_b)
# print(b.get_AVE())




