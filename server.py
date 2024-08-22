import os
import socket
import math
import json
import sys

# 実数xを最も近い整数に切り捨てる
def floor(x):
    res = math.floor(x)
    print(f'Truncate real {x} to the nearest integer')
    return [res, type(res).__name__]

# xのn乗根を計算する
def nroot(array):
    n = array[0]
    x = array[1]
    res = math.pow(x, 1/n)
    print(f'Compute {n}-square root of {x}')
    return [res, type(res).__name__]

# 文字列を逆順にする
def reverse(s):
    print('reversing the string...')
    return [s[::-1], type(s).__name__]

# 2つの文字列がアナグラムであるかどうかを判断する
def validAnagram(array):
    print('Check Anagram...')
    s1 = array[0]
    s2 = array[1]
    res = False
    if len(s1) != len(s2):
        res = False
    
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
            res = False
    
    if max(hash.values()) == 0:
        res = True
    
    return [res, type(res).__name__]

# 配列をソートする
def sort(strArr):
    print('sort string array')
    return [sorted(strArr), type(strArr).__name__]

# 関数の目次
functions = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort
}

response = {
    "results": "",
    "result_type": "",
    "id": 0
}

# サーバとクライアントの接続
def connection():
    # UNIXソケットをストリームモードで作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    server_address = './server_socket_file'
    # 以前の接続の削除
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print(f'Starting up on {server_address}')
    
    # サーバアドレスにソケットを接続する
    sock.bind(server_address)

    sock.listen(1)

    while True:
        # クライアントからの接続受け入れ
        connection, client_address = sock.accept()

        try:
            while True:
                
                data = connection.recv(4096)
                # データがあればデータの処理を行い、クライアントに返却する。
                if data:
                    request = json.loads(data.decode('utf-8'))
                    print(f'received data: {request}')

                    funcResponse = handleRequest(request)

                    # responseの作成
                    response["results"] = funcResponse[0]
                    response["result_type"] = funcResponse[1]
                    response["id"] += 1
                    print(response)
                    connection.send(json.dumps(response).encode())
                    connection.shutdown(1)

                else:
                    break
        finally:
            print('Closing current connection')
            connection.shutdown(1)
            connection.close()
            sys.exit()



# リクエストを処理する
def handleRequest(request):
    try:
        result = functions[request['method']](request['params'])
        return result
    except Exception as error:
        raise error

connection()