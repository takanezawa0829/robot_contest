# RobotContest
知能ロボットコンテストのための王研究室A班によるロボット作成プロジェクト。

# Documents
図やデータシート、書類などを保存して共有する。

# 気をつけてほしいこと
* pip3 install した時、以下のコマンドを実行してほしい。
```
sh export_pip3_lib.sh
```

# Ubuntu20.04LTSでROS1の環境構築をする。
## Python3の設定をする。
1. Ubuntuを更新する。
```
sudo apt update
sudo apt -y upgrade
```
2. pip3をinstallする。
```
sudo apt install -y python3-pip
```
3. Python3のpackageと開発ツールをinstallしておく。
```
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```
4. Python3の仮想環境、venvをinstallする。
```
sudo apt install -y python3-venv
```

## ROS1の環境構築をする。
1. source.listの設定
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. キーの設定をする。
```
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
3. ROS1をinstallする。
```
sudo apt update
sudo apt install ros-noetic-desktop-full
```
4. 環境設定をする。
```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```
5. rosdepの初期化をする。
```
sudo rosdep init
rosdep update
```

## ワークスペースを設定する。
1. bash.rcに少し追記する。
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
2. bash.rcにcatkin_wsを有効にするための記述を追加する。
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```














