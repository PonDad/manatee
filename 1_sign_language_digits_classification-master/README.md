## TensorFlow.jsで「じゃんけん」を判別してみよう

![PC-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/sign-language-digits.gif)

[Demo: sign-language-digits-tfjs](https://sign-language-digits-tfjs.herokuapp.com/)

### インストール

```bash
$ git clone https://github.com/PonDad/manatee.git
$ cd manatee/1_sign_language_digits_classification-master/nodejs/
$ npm install
$ npm start
```

### 使い方

リンクを開いてください `http://localhost:8080/`

![ScreenShot-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/Screenshot.png)

1. 「スタート」ボタンで学習済みモデルをTensorFlow.jsをつかって読み込み、Webカメラを起動させます。

2. 「推論」ボタンでWebカメラの画像をクリップしcanvas要素へと変換します。画像はTensorFlow.jsをつかいテンソル形式へ変換し、学習済みモデルをつかって10クラスの分類をおこないます。

3. 「推論」は`setInterval()`メソッドをつかって0.1秒ごとに実行します。終了する際は「クリア」ボタンで画面をリロードします。

### データセット

Apacheライセンス2.0で公開されているデータセット [ardamavi/Sign Language Digits Dataset](https://github.com/ardamavi/Sign-Language-Digits-Dataset) を使用しています。

![Digits-image](https://raw.githubusercontent.com/PonDad/manatee/master/1_sign_language_digits_classification-master/nodejs/static/img/digit.png)

トルコのANKARA高校の皆さんで作成したデータセットです。
