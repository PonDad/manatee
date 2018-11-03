## TensorFlow.jsで「感情」を認識してみよう

![demo](https://raw.githubusercontent.com/PonDad/manatee/master/2_emotion_recognition-master/nodejs/static/img/emotion_demo.gif)

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

### 学習済みモデルの取得

感情認識の学習済みモデルは公開レポジトリ[oarriaga/face_classification - GitHub](https://github.com/oarriaga/face_classification) より取得します。

![facerecognition](https://raw.githubusercontent.com/PonDad/manatee/master/2_emotion_recognition-master/nodejs/static/img/oarriaga%3Aface_classification.png)

ドイツにあるBonn-Rhein-Sieg 応用科学大学の研究グループが公開しているレポジトリです。ロボティックス分野の顔認識や音声認識などを使った自律システムを専門に研究しているようですね。

性別認識と感情認識の学習済みモデルが公開されており、デモプログラムを使ってOpenCVの画像で認識結果を表示することができます。

レポジトリの中で性別認識はIMDBデータセット、感情認識は fer2013データセットを使用しているとあります。独自のデータセットを用いての学習も可能です。

感情認識のfer2013データセット[Challenges in Representation Learning: Facial Expression Recognition Challenge - Kaggle](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)はKaggleのコンペ対象にもなっています。

![Kaggle](https://raw.githubusercontent.com/PonDad/manatee/master/2_emotion_recognition-master/nodejs/static/img/kaggle.png)

CSVデータには画像サイズ48x48ピクセルの白黒画像（色調0~255の1チャンネル画像）3,589枚分のデータが収められています。

ラベルが0~6になっており、（0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral）7つの感情分類に分ける分類問題です。