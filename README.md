# get-MACaddress-from-COM-port

## JP

## 概要・使用方法:

USBにつないだ機器のMACアドレスを取得する.  
第一引数にUSBデバイスが使用するポート名を与える.（WindowsはCOM?、Linuxは/dev/ttyUSB0やttyACM0）  
MACアドレスは以下の2つのフォーマット形式で出力される.

``` sh
$ python getMacAddrFromCOM.py COM8
FF:FF:FF:FF:FF:FF
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF
```

## 使用要件:

機器を接続しているCOMポート名は、別途デバイスマネージャーなどで調べておくこと.

- COMポートの表示形式
  - Windows : COM8
  - Linux : /dev/ttyUSB0やttyACM0

esptoolを使用するため事前にインストールしておくこと.

``` sh
$ pip install esptool
```

`subprocess.run` 時に `sys.executable -m esptool` コマンドで実行しており、Windows, Linux両方で動作する想定です。

## EN

## Overview & Usage:

This script retrieves the MAC address of a device connected via USB.  
Pass the port name used by the USB device as the first argument.  (ex. Windows: COM8, Linux: /dev/ttyUSB0 or ttyACM0)
The MAC address will be output in the following two formats:

```sh
$ python getMacAddr.py COM8
FF:FF:FF:FF:FF:FF
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF
```

Make sure to check the COM port name of the connected device using Device Manager or an equivalent tool.

- COM port format:
  - Windows: COM8
  - Linux: /dev/ttyUSB0 or /dev/ttyACM0

Pre-install esptool before running the script:

```sh
sh
$ pip install esptool
```

The script executes esptool using the sys.executable -m esptool command within subprocess.run, ensuring compatibility with both Windows and Linux.
