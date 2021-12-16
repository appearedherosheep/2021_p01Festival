import sys
from PyQt5.QtCore import QByteArray
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
        # self.center()
        self.initUI()
        self.show_img()
        self.showMaximized()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        title_label = QLabel('너의 얼굴은')
        title_label.setFont(QFont('나눔바른고딕',30))

        self.label = QLabel()
        self.animal_label = QLabel()

        label_hbox = QHBoxLayout()
        label_hbox.addWidget(self.label)
        label_hbox.addWidget(self.animal_label)
        
        self.show_img()
        
        self.start_btn = QPushButton('start')
        self.stop_btn = QPushButton('stop')
        self.save_btn = QPushButton('save')

        btn_hbox = QHBoxLayout()
        btn_hbox.addWidget(self.start_btn)
        btn_hbox.addWidget(self.stop_btn)
        btn_hbox.addWidget(self.save_btn)

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.save_btn.clicked.connect(self.save)

        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
        vbox.addLayout(label_hbox)
        vbox.addLayout(btn_hbox)  
        self.setLayout(vbox)

    def opencv(self):
        cap = cv2.VideoCapture(0)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.label.resize(width, height)

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
                self.label.setPixmap(pixmap)
                
        cap.release()
        print("Thread end.")

    def start(self):
        self.running = True
        th = threading.Thread(target=self.opencv)
        th.start()
        print("started..")

    def stop(self):
        self.running = False
        print("stoped..")

    def save(self):
        time.sleep(3)
        cv2.imwrite('captured.jpg', self.img)
        self.show_animal()

    def show_animal(self):
        predict_animal = predict('captured.jpg')
        src = f'animal/{predict_animal}.jpg'
        self.animal_label.setPixmap(QPixmap(src))

    def show_img(self) :
        src = 'loading.gif'
        self.gif_movie = QMovie(src,QByteArray(),self)
        self.gif_movie.setCacheMode(QMovie.CacheAll)
        
        self.animal_label.setMovie(self.gif_movie)
        self.gif_movie.start()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
