## TensorFlow.jsで「感情」を判別してみよう

![screenShot]()

[Demo](https://emotion-recognition-tfjs.herokuapp.com/)

### インストール

```bash
$ git clone https://github.com/PonDad/manatee.git
$ cd manatee/2_emotion_recognition-master/nodejs/
$ npm install
$ npm start
```

### 使い方

リンクを開いてください　http://localhost:8080/

![Screenshot](https://raw.githubusercontent.com/PonDad/manatee/master/2_emotion_recognition-master/nodejs/static/img/Screenshot.png)

1. 「スタート」ボタンで学習済みモデルをTensorFlow.jsをつかって読み込み、Webカメラを起動させます。

2. 「推論」ボタンで[tracking.js](https://trackingjs.com/)を使い、Webカメラの画像から顔部分をクリップしcanvas要素へと変換します。画像はTensorFlow.jsをつかいテンソル形式へ変換し、学習済みモデルをつかって7クラスの分類をおこないます。

3. 終了する際は「クリア」ボタンで画面をリロードします。

### データセット

Kaggleで公開されているデータセット[Challenges in Representation Learning: Facial Expression Recognition Challenge - Kaggle](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)を使用します。

Pythonでの学習は[oarriaga/face_classification - GitHub](https://github.com/oarriaga/face_classification)
ドイツのBonn-Rhein-Sieg応用化学大学の研究グループが公開しているレポジトリを使用します。