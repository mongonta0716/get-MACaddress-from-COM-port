# get-MACaddress-from-COM-poat

## JP

## 概要・使用方法:

USBにつないだ機器のMACアドレスを取得する.  
第一引数にUSBデバイスが使用するCOMポートの番号を与える.  
MACアドレスは以下の2つのフォーマット形式で出力される.

``` sh
$ python getMacAddrFromCOM.py 8
FF:FF:FF:FF:FF:FF
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF
```

## 使用要件:

機器を接続しているCOMポートの番号は、別途デバイスマネージャーなどで調べておくこと.

esptoolを使用するため事前にインストールしておくこと.

``` sh
$ pip install esptool
```

esptool.pyへのパスを正しく通しておくこと.  
下記は一例、esptool.pyの場所を正しく指定する.


``` sh
$ PATH=$HOME/.local/bin:$PATH
```

## EN

## Overview & Usage:

This script retrieves the MAC address of a device connected via USB.  
Pass the COM port number used by the USB device as the first argument.  
The MAC address will be output in the following two formats:

```sh
$ python getMacAddr.py 8
FF:FF:FF:FF:FF:FF
0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF
```

## Requirements:

Check the COM port number of the connected device using Device Manager or another tool beforehand.

Install esptool before running the script:

```sh
sh
$ pip install esptool
```
Ensure that the path to esptool.py is correctly set.
The following is an example—adjust the path according to your environment:

``` sh
$ PATH=$HOME/.local/bin:$PATH
```


