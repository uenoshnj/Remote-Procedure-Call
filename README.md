# Remote-Procedure-Call
## 概要
異なるプログラミング言語で書かれたクライアントとサーバが共通の方法で通信し、クライアントから指定された特定の関数をサーバが実行する。<br>
サーバ：Python<br>
クライアント：JavaScript(Node.jsを使用)

## リクエストとレスポンスの形式
JSON形式のメッセージを使用する

### ・リクエスト
* メソッドの名前
* 引数
* 引数の型
* リクエストID

#### 例
```json
{
   "method": "nroot", 
   "params": [3, 8], 
   "param_types": ["int", "int"],
   "id": 1
}
```

### ・レスポンス
* 結果
* 結果の型
* リクエストID

#### 例
```json
{
   "results": 2,
   "result_type": "int",
   "id": 1
}
```

## サーバが提供する関数
* floor(double x)<br>
10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
* nroot(int n, int x)<br>
方程式 $r^n = x$　における、r の値を計算する。
* reverse(string s)<br>
文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
* validAnagram(string str1, string str2)<br>
2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
* sort(string[] strArr)<br>
文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。