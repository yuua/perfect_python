+ P126から

#### 前の復習

#### ジェネレータ

+ ジェネレータはイテレーターの一種

> ジェネレータ関数はyield式を含む __next__() メソッドが呼ばれる旅胃yield式まで実行される

+ ex フィボナッチ数列

```fib.py
def fib:
  a,b = 0,1
  while True:
    yield a
    a,b = b, a+b
```

+ fib.pyを使って最初の10要素を取得する処理

```gene.py
items = []
for v in fib():
  items.append(v)
  if len(items) > 10:
    break
```

#### ちなみに

+ __next__() 以外にも

1. send()

```
def test(a):
  b = 0
  while True:
    v = a + b
    a = yield v
```
> send()で指定した値はyieldの値になる send(20) とかすると 20がaにわたったりする (関数実行してから) a = test(1) とかして a.send()

2. throw()

> 見ての通り再会待ちのジェネレータに例外を投げるメソッド

3. close()

> ジェネレータをquitする

+ 4つくらいメソッドがサポートされてる
