# coding:utf8

print("例外処理")

# 基本は

try:
    10/0
# asで一次変数としてエラーを受け取れる
except ZeroDivisionError as  e:
    print(type(e))
finally
    print("最後に実行されるよん")






