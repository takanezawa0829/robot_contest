import numpy as np

# uart通信のポート設定
serial_port = '/dev/ttyUSB0'
serial_timeout = 1

# サーボの数値データが1増えると何度増えるか
data_rad_diff = 0.24

# サーボを制御するための設定
foot = {
    # 前脚
    'front': {
        'left': {
            'id': [1, 2, 3], # サーボのID [第1関節, 第2関節, 第3関節]
            'rev': ['rev1', 'rev2', 'rev3'], # urdfのjointの名前 [第1関節, 第2関節, 第3関節]
            'standard': [500, 500, 200], # 関節角度が0度のときのサーボモータの値 [500, 500, 200]付近を推薦
            'reverse': [True, True, False], # サーボの回転方向を逆にするか [第1関節, 第2関節, 第3関節]
        },
        'right': {
            'id': [4, 5, 6], # サーボのID [第1関節, 第2関節, 第3関節]
            'rev': ['rev4', 'rev5', 'rev6'], # urdfのjointの名前 [第1関節, 第2関節, 第3関節]
            'standard': [500, 500, 200], # 関節角度が0度のときのサーボモータの値 [500, 500, 200]付近を推薦
            'reverse': [True, False, True], # サーボの回転方向を逆にするか [第1関節, 第2関節, 第3関節]
        },
    },
    # 真ん中の脚
    'middle': {
        'left': {
            'id': [7, 8, 9], # サーボのID [第1関節, 第2関節, 第3関節]
            'rev': ['rev7', 'rev8', 'rev9'], # urdfのjointの名前 [第1関節, 第2関節, 第3関節]
            'standard': [500, 500, 600], # 関節角度が0度のときのサーボモータの値 [500, 500, 200]付近を推薦
            'reverse': [True, False, True], # サーボの回転方向を逆にするか [第1関節, 第2関節, 第3関節]
        },
        'right': {
            'id': [10, 11, 12], # サーボのID [第1関節, 第2関節, 第3関節]
            'rev': ['rev10', 'rev11', 'rev12'], # urdfのjointの名前 [第1関節, 第2関節, 第3関節]
            'standard': [500, 500, 200], # 関節角度が0度のときのサーボモータの値 [500, 500, 200]付近を推薦
            'reverse': [True, False, True], # サーボの回転方向を逆にするか [第1関節, 第2関節, 第3関節]
        },
    },
    # 後ろ脚
    'end': {
        'left': {
            'id': [13, 14, 15], # サーボのID [第1関節, 第2関節, 第3関節]
            'rev': ['rev13', 'rev14', 'rev15'], # urdfのjointの名前 [第1関節, 第2関節, 第3関節]
            'standard': [300, 500, 200], # 関節角度が0度のときのサーボモータの値 [500, 500, 200]付近を推薦
            'reverse': [True, True, False], # サーボの回転方向を逆にするか [第1関節, 第2関節, 第3関節]
        },
        'right': {
            'id': [16, 17, 18], # サーボのID [第1関節, 第2関節, 第3関節]
            'rev': ['rev16', 'rev17', 'rev18'], # urdfのjointの名前 [第1関節, 第2関節, 第3関節]
            'standard': [500, 500, 200], # 関節角度が0度のときのサーボモータの値 [500, 500, 200]付近を推薦
            'reverse': [True, False, True], # サーボの回転方向を逆にするか [第1関節, 第2関節, 第3関節]
        },
    },
}

# Publishされたjoint_statesの回数を数えるために使用(変更禁止)
count = 0
