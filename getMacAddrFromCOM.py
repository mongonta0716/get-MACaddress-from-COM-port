# 概要:
# USBにつないだ機器のMACアドレスを取得する
# MACアドレスは以下の2つのフォーマット形式で出力される
# 機器を接続しているCOMポートの番号は、別途デバイスマネージャーなどで調べておくこと
# 
# dc:54:75:cf:1d:50
# 0xdc, 0x54, 0x75, 0xcf, 0x1d, 0x50
# 
# 使用要件:
# esptoolを使用するため事前にインストールしておくこと
# $ pip install esptool
# esptool.pyへのパスを正しく通しておくこと(下記は例、esptool.pyの場所を正しく指定する)
# $ PATH=$HOME/.local/bin:$PATH
# 
# 使用方法:
# 第一引数にポート名を与える(Windows: COM8, Linux: /dev/ttyUSB0orACM0)
# $ python getMacAddr.py COM8
# FF:FF:FF:FF:FF:FF
# 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF

import subprocess
import sys
import re
import shutil

def get_mac_address(com_port):
    try:
        # esptool コマンドを実行
        esptool_path = shutil.which("esptool.py")
        result = subprocess.run([
            esptool_path, "--port", com_port, "read_mac"
        ], capture_output=True, text=True, check=True)
        
        # 標準出力からMACアドレスを抽出
        match = re.search(r'(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', result.stdout)
        if match:
            mac = match.group(1)
            print(mac)
            # 変換して出力
            formatted_mac = ', '.join(f'0x{x}' for x in mac.split(':'))
            print(formatted_mac)
        else:
            print("MACアドレスが見つかりませんでした。")
    except subprocess.CalledProcessError as e:
        print("エラー: esptoolの実行に失敗しました。", e)
    except Exception as e:
        print("エラー: ", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python getMacAddr.py <ポート名>")
        sys.exit(1)
    
    com_port = sys.argv[1]
    get_mac_address(com_port)
