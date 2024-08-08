import os
import socket
import math
import json

# 実数xを最も近い整数に切り捨てる
def floor(x):
    return math.floor(x)

# xのn乗根を計算する
def nroot(n, x):
    return math.pow(x, 1/n)

# 文字列を逆順にする
def reverse(s):
    return s[::-1]

# 2つの文字列がアナグラムであるかどうかを判断する
def validAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    hash = {}
    for s in s1:
        if s in hash:
            hash[s] += 1
        else:
            hash[s] = 1
    
    for c in s2:
        if c in hash:
            hash[c] -= 1
        else:
            return False
    
    if max(hash.values()) == 0:
        return True
    
    return False

# 配列をソートする
def sort(strArr):
    return sorted(strArr)

# 関数の目次
functions = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort
}

# サーバとクライアントの接続
def connection():
    # UNIXソケットをストリームモードで作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    # UNIXソケットのパスが記載されたjsonファイルの読み込み
    config = json.load(open('config.json'))

    # UNIXソケットのパスを設定
    server_address = config['server_address']

    # 以前の接続の削除
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print(f'Starting up on {server_address}')
    
    # サーバアドレスにソケットを接続する
    sock.bind(config['server_address'])

    sock.listen(1)

    while True:
        # クライアントからの接続受け入れ
        connection, client_address = sock.accept()

        try:
            while True:
                data = connection.recv(4096)

                if data:
                    request = json.loads(data)
                    handleRequest(request)
                else:
                    break
        finally:
            print('Closing current connection')
            connection.close()


def handleRequest(request):
    try:
        result = functions[request['method']](*request['params'])
        return result
    except Exception as error:
        raise error
