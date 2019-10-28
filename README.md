# atcoder_checksamples
AtCoderのサンプルをまとめてテストします

AtCoderのサンプルをまとめてテスト出来るだけのツールです。
問題の例題と解答を引っ張ってきて、自分のコードの出力と一致するかだけを判断します。

## Usage
atcoder_checksamples.pyを実行。
開催されるコンテストの名前と番号に合わせたデータを入力。
Beginer:abc,Regular:arc,Grand:agc

```
$ python atcoder atcoder_checksamples.py --c_n abc010 --p_n a --f hoge.py #abc010のa問題をhoge.pyでテスト
```


## Environment
Python3

Ubuntu18.04
