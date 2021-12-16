import sys
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtGui import QFont, QImage, QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QDesktopWidget
import cv2
import threading
from tm import predict


class MyApp(QWidget):
    def __init__(self):
        self.running = False

        super().__init__()
        self.setWindowTitle('너의 얼굴은')
        self.initUI()
        self.start_cam()
        self.showMaximized()

    def initUI(self):
        # 상단 제목
        self.title_label = QLabel('너의 얼굴은...')
        self.title_label.setFont(QFont('나눔바른고딕', 100))
        self.title_label.setAlignment(Qt.AlignCenter)

        # 중간 왼쪽 vbox
        # opencv_label = QLabel('너의 얼굴')
        # opencv_label.setFont(QFont('나눔바른고딕', 50))
        # opencv_label.setAlignment(Qt.AlignCenter)
        self.cam_label = QLabel()

        left_vbox = QVBoxLayout()
        # left_vbox.addStretch(0)
        left_vbox.addWidget(self.cam_label)
        # left_vbox.addWidget(opencv_label)

        # 중간 오른쪽
        self.animal_label = QLabel()

        # 로딩중
        self.gif_movie = QMovie('loading (2).gif', QByteArray(), self)
        self.gif_movie.setCacheMode(QMovie.CacheAll)
        self.animal_label.setMovie(self.gif_movie)

        self.cam_label.setMovie(self.gif_movie)
        self.gif_movie.start()

        # 중간 hbox
        label_hbox = QHBoxLayout()
        label_hbox.addStretch(1)
        label_hbox.addLayout(left_vbox)
        label_hbox.addStretch(1)
        label_hbox.addWidget(self.animal_label)
        label_hbox.addStretch(1)

        # 아래 hbox
        self.capture_btn = QPushButton('찰칵')
        self.capture_btn.setFixedSize(300, 180)
        self.capture_btn.setFont(QFont('나눔바른고딕', 70))

        # self.retry_btn = QPushButton('리트')
        # self.retry_btn.setFixedSize(300, 180)
        # self.retry_btn.setFont(QFont('나눔바른고딕', 70))

        btn_hbox = QHBoxLayout()
        btn_hbox.addStretch(1)
        btn_hbox.addWidget(self.capture_btn)
        # btn_hbox.addWidget(self.retry_btn)
        btn_hbox.addStretch(1)

        self.capture_btn.clicked.connect(self.capture)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addStretch(1)
        vbox.addLayout(label_hbox)
        vbox.addStretch(1)
        vbox.addLayout(btn_hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def opencv(self):
        self.running = True
        cap = cv2.VideoCapture(0)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.cam_label.resize(width, height)

        while self.running:
            ret, self.img = cap.read()
            if ret:
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                self.img = cv2.flip(self.img, 1)
                h, w, c = self.img.shape
                qImg = QImage(
                    self.img.data,
                    w,
                    h,
                    w*c,
                    # self.img.strides[0],
                    QImage.Format_RGB888
                )
                pixmap = QPixmap.fromImage(qImg)
                self.cam_label.setPixmap(pixmap)

        cap.release()
        print("Thread end.")

    def start_cam(self):
        self.running = True
        th = threading.Thread(target=self.opencv)
        th.start()
        print("started..")

    def capture(self):
        # print(1)
        # time.sleep(3)
        # print(2)
        cv2.imwrite('captured.jpg', self.img)
        # print(3)
        self.show_animal()

    def show_animal(self):
        predict_animal = predict('captured.jpg')
        src = f'animal/{predict_animal[0]}.jpg'
        self.animal_label.setPixmap(QPixmap(src))
        self.title_label.setText(
            f'너의 얼굴은 {int(predict_animal[2]*100)}% {predict_animal[1]}'
            )

    # def show_img(self):
    #     src = 'loading (2).gif'
    #     self.gif_movie = QMovie(src, QByteArray(), self)
    #     self.gif_movie.setCacheMode(QMovie.CacheAll)
    #     self.animal_label.setMovie(self.gif_movie)
    #     self.gif_movie.start()

    # def show_img(self):
    #     src = 'loading (2).gif'
    #     self.gif_movie = QMovie(src, QByteArray(), self)
    #     self.gif_movie.setCacheMode(QMovie.CacheAll)
    #     self.animal_label.setMovie(self.gif_movie)
    #     self.gif_movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
