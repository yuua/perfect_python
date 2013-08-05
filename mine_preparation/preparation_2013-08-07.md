#### 8/7用の予習

+ 個人的予習

##### __name__とか

+ これはスクリプトファイルの時だけ__main__がはいる

> インタラクティブシェルとかでpythonを実行してみるよわかる

```python.py
Python 2.7.1 (r271:86832, Jul 31 2011, 19:30:53) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> __name__
'__main__'
>>>
```

こんな感じ

```python.py
# coding: utf-8

def main:
  print("インタラクティブだけ")

print("importでもいけるよ")

if __name__ == "__main__":
  main()

```

+ こんなの用意しておくんで python unko.pyとかやると両方標準出力ででる

```import.py
import unko.py
```

+ これだとimportでもいけるよだけprintされたりする

