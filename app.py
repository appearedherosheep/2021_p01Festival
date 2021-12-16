import sys
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtGui import QFont, QImage, QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QDesktopWidget
import cv2
import threading
import time
from tm import predict


class MyApp(QWidget):
    def __init__(self):
        self.running = False
        
        super().__init__()
        self.setWindowTitle('너의 얼굴은')
        self.initUI()
        self.start_cam()
        # self.show_img()
        self.showMaximized()

    def initUI(self):
        # 상단 제목
        title_label = QLabel('너의 얼굴은')
        title_label.setFont(QFont('나눔바른고딕', 100))
        title_label.setAlignment(Qt.AlignCenter)
        
        # 중간 왼쪽 vbox
        opencv_label = QLabel('너의 얼굴')
        opencv_label.setFont(QFont('나눔바른고딕', 50))
        opencv_label.setAlignment(Qt.AlignCenter)
        self.cam_label = QLabel()

        left_vbox = QVBoxLayout()
        left_vbox.addStretch(0)
        left_vbox.addWidget(self.cam_label)
        left_vbox.addWidget(opencv_label)
        
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
        self.stop_btn = QPushButton('stop')
        self.save_btn = QPushButton('save')

        btn_hbox = QHBoxLayout()
        btn_hbox.addWidget(self.stop_btn)
        btn_hbox.addWidget(self.save_btn)

        self.save_btn.clicked.connect(self.save)

        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
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

    def save(self):
        print(1)
        time.sleep(3)
        print(2)
        cv2.imwrite('captured.jpg', self.img)
        print(3)
        self.show_animal()

    def show_animal(self):
        predict_animal = predict('captured.jpg')
        src = f'animal/{predict_animal}.jpg'
        self.animal_label.setPixmap(QPixmap(src))

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
