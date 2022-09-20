#!/usr/bin/python3
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy
from robot_contest.msg import OutputCsv
# ディレクトリを操作するためのモジュールをimport
import os
# csvファイルを操作するためのモジュールをimpot
import csv
# 時刻を取得するためのモジュールをimport
import datetime

# csvファイルをlogディレクトリに作成する関数（ファイル名は実行した時刻）
def make_csv():
    global now_str
    # logディレクトリが存在していなければ新たに作成
    if not os.path.exists('./log/'):
        os.mkdir('log')
    # ファイルを作成
    with open(f'log/{now_str}.csv', 'w') as csv_file:
        csv_file.write('')

# csvファイルにヘッダーを入力する関数
def output_header(header):
    global now_str
    with open(f'log/{now_str}.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()


# csvファイルにデータを入力する関数
def output_data(header, data):
    global now_str
    with open(f'log/{now_str}.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writerow(data)

# 最初に呼ばれた時だけtrueを返す関数
def getFlag():
    flag = getFlag.flag
    getFlag.flag = False
    return flag
getFlag.flag = True

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義
def callback(data):
    # ヘッダーをheader_listに代入
    header_list = []
    for header in data.header:
        header_list.append(header)

    # データをrowに代入
    value = {}
    for i in range(len(data.header)):
        value[data.header[i]] = data.value[i]

    # 初めの1度だけ実行
    if getFlag():
        output_header(header_list)

    # 受け取ったデータをコンソールに出力
    print(value)

    # 受け取ったデータをcsvに出力
    output_data(header_list, value)



def output_csv():
    rospy.init_node('output_csv', anonymous=True)

    # 現在時刻を取得
    now = datetime.datetime.now()
    global now_str
    now_str = now.strftime('%Y_%m_%d_%H_%M_%S')

    # csvファイルを作成
    make_csv()

    # Subscriberとしてoutput_csvというトピックに対してSubscribeし、topicが更新されたときはcallbackという名前のコールバック関数を実行
    rospy.Subscriber('output_csv', OutputCsv, callback)

    # topic更新の待ちうけを行う関数
    rospy.spin()


if __name__ == '__main__':
    # 実際にsubscribeする関数を呼び出し
    output_csv()


