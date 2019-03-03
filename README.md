# atcoder_checksamples
AtCoderのサンプルをまとめてテストします

AtCoderのサンプルをまとめてテスト出来るだけのツールです。
問題の例題と解答を引っ張ってきて、自分のコードの出力と一致するかだけを判断します。

## Usage
atcoder_checksamples.pyを取得し、同じフォルダ内にsettingを作成。
開催されるコンテストの名前と番号に合わせたデータを入力。

```:setting
#setting
arc000
```
Beginer:abc,Regular:arc,Grand  :agc

settingを準備したらatcoder_checksamples.pyを実行。
```
$ python atcoder atcoder_checksamples.py a hoge.exe #a問題をhoge.pyでテスト
```

## Environment
Python3

Ubuntu18.04
