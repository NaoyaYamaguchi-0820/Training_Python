# コメントは行頭に#をつける ショートカット→Ctrl /

#コンソールに表示する
print("Hello World")

# 変数を定義する。Pythonは動的型付けなので型を定義する必要はない
a = 1
b = 2
print(a + b)

# 定義されていない変数を呼ぶとエラーになる
# print(c)

# ライブラリをインポートすることで、様々な便利機能が使える
# サンプル カレントディレクトリを返す関数
import os
print(os.getcwd())

# オブジェクトの型を調べる
print(type(1))
print(type("Hello"))
print(type(1.0))

# オブジェクトの属性一覧を取得する
string = "Hello World"
print(dir(string))

# stringのupper属性を調べてみる。すべて大文字にした文字列が返ってくる
print(string.upper())




