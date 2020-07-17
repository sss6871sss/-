### 概要
来客者を人感センサーで検出して、顔を識別して顔写真を撮り、
顔写真をチャットツール（Slack）に通知します。
(おまけに人感センサーが反応すると音声が出ます。)
### 環境
- 必要な物
  - Raspberry Pi 3 B+
  - HCSR501 モーションセンサー
  - PiCamera
  - ジャンパーワイヤー
- version
  - opencv 4.1.1
  - python 3以上

### 条件
Slackのアカウント、ワークスペース,appが必要です。

### 使い方

`$python3 detectSensor.py`
で起動
