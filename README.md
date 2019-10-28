# atcoder_checksamples
AtCoderのサンプルをまとめてテストします

AtCoderのサンプルをまとめてテストするツールです。
問題の例題と解答を引っ張ってきて、自分のコードの出力と一致するかを判断します。

## Usage
atcoder_checksamples.pyを実行する。
コマンドライン引数として開催されるコンテストの名前と番号に合わせたデータを入力。


```
$ python atcoder atcoder_checksamples.py --c_n abc010 --p_n a --f hoge.py #abc010のa問題をhoge.pyでテスト
```
##コンテストネーム
Beginer:abc,Regular:arc,Grand:agc

## Environment
Python3

Ubuntu18.04
