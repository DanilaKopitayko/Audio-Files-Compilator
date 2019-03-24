#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os,codecs
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QVBoxLayout, QFileSystemModel
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QColorDialog, QFileDialog
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import  QBrush, QPalette, QPixmap#, Qimage
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtMultimedia import *
import pygame
from pygame import mixer
from pydub import AudioSegment
#import mutagen.mp3


#AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"
#AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        label = QLabel(self.centralwidget)
        pixmap = QPixmap(r'background.jpg')
        label.setPixmap(pixmap)
        MainWindow.setFixedSize(pixmap.width(),pixmap.height())



        self.rockbt = QtWidgets.QRadioButton(self.centralwidget)
        self.rockbt.setGeometry(QtCore.QRect(10, 56, 57, 20))
        self.rockbt.setObjectName("rockbt")
        self.rockbt.setFont(QtGui.QFont("SansSerif",12))
        self.genre = QtWidgets.QButtonGroup(MainWindow)
        self.genre.setObjectName("genre")
        self.genre.addButton(self.rockbt)
        self.popbt = QtWidgets.QRadioButton(self.centralwidget)
        self.popbt.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.popbt.setObjectName("popbt")
        self.popbt.setFont(QtGui.QFont("SansSerif",12))
        self.genre.addButton(self.popbt)
        self.countrybt = QtWidgets.QRadioButton(self.centralwidget)
        self.countrybt.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.countrybt.setObjectName("countrybt")
        self.countrybt.setFont(QtGui.QFont("SansSerif",12))
        self.genre.addButton(self.countrybt)
        self.jazzbt = QtWidgets.QRadioButton(self.centralwidget)
        self.jazzbt.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.jazzbt.setObjectName("jazzbt")
        self.jazzbt.setFont(QtGui.QFont("SansSerif",12))
        self.genre.addButton(self.jazzbt)
        self.classicalbt = QtWidgets.QRadioButton(self.centralwidget)
        self.classicalbt.setGeometry(QtCore.QRect(10, 180, 82, 17))
        self.classicalbt.setObjectName("classicalbt")
        self.classicalbt.setFont(QtGui.QFont("SansSerif",12))
        self.genre.addButton(self.classicalbt)
        self.bluesbt = QtWidgets.QRadioButton(self.centralwidget)
        self.bluesbt.setGeometry(QtCore.QRect(10, 210, 82, 17))
        self.bluesbt.setObjectName("bluesbt")
        self.bluesbt.setFont(QtGui.QFont("SansSerif",12))
        self.genre.addButton(self.bluesbt)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("SansSerif",15))
        self.label.setGeometry(QtCore.QRect(220,10 , 500, 41))
        self.volumelb = QtWidgets.QLabel(self.centralwidget)
        self.volumelb.setObjectName("volumelb")
        self.volumelb.setGeometry(QtCore.QRect(598, 432, 41, 41))
        self.volumelb.setFont(QtGui.QFont("SansSerif",15))
        #self.volumelb.setStyleSheet('border-style: solid; border-width: 2px; border-colour: black;')
        self.name1 = QtWidgets.QLabel(self.centralwidget)
        self.name1.setObjectName("name1")
        self.name1.setStyleSheet('border-style: solid; border-width: 2px; border-colour: black ')
        self.name1.setFont(QtGui.QFont("SansSerif",12))
        self.name1.setGeometry(QtCore.QRect(220,77, 115, 30))
        self.name2 = QtWidgets.QLabel(self.centralwidget)
        self.name2.setStyleSheet('border-style: solid; border-width: 2px; border-colour: black ')
        self.name2.setFont(QtGui.QFont("SansSerif",12))
        self.name2.setObjectName("name2")
        self.name2.setGeometry(QtCore.QRect(490,77, 115, 30))

        layout = QVBoxLayout()
        layout.addWidget(self.rockbt)
        layout.addWidget(self.popbt)
        layout.addWidget(self.countrybt)
        layout.addWidget(self.jazzbt)
        layout.addWidget(self.classicalbt)
        layout.addWidget(self.bluesbt)

        self.lb1 = QtWidgets.QLabel(self.centralwidget)
        self.lb1.setGeometry(QtCore.QRect(10, 10, 105, 41))
        self.lb1.setObjectName("lb1")
        self.lb1.setFont(QtGui.QFont("SansSerif",12))
        self.lb2 = QtWidgets.QLabel(self.centralwidget)
        self.lb2.setGeometry(QtCore.QRect(10, 250, 105, 51))
        self.lb2.setFont(QtGui.QFont("SansSerif",12))
        self.lb2.setObjectName("lb2")
        self.bpm60 = QtWidgets.QRadioButton(self.centralwidget)
        self.bpm60.setGeometry(QtCore.QRect(10, 300, 82, 17))
        self.bpm60.setObjectName("bpm60")
        self.bpm60.setFont(QtGui.QFont("SansSerif",12))
        self.tempo = QtWidgets.QButtonGroup(self.centralwidget)
        self.tempo.setObjectName("tempo")
        self.tempo.addButton(self.bpm60)
        self.bpm120 = QtWidgets.QRadioButton(self.centralwidget)
        self.bpm120.setGeometry(QtCore.QRect(10, 330, 82, 17))
        self.bpm120.setObjectName("bpm120")
        self.bpm120.setFont(QtGui.QFont("SansSerif",12))
        self.tempo.addButton(self.bpm120)
        self.bpm180 = QtWidgets.QRadioButton(self.centralwidget)
        self.bpm180.setGeometry(QtCore.QRect(10, 360, 82, 17))
        self.bpm180.setObjectName("bpm180")
        self.bpm180.setFont(QtGui.QFont("SansSerif",12))
        self.tempo.addButton(self.bpm180)




        '''self.abc = QtWidgets.QRadioButton(self.centralwidget)
        self.abc.setGeometry(QtCore.QRect(100, 360, 82, 17))
        self.bpm180.setObjectName("abc")'''




        self.musicbt = QtWidgets.QPushButton(self.centralwidget)
        self.musicbt.setGeometry(QtCore.QRect(10, 390, 91, 31))
        self.musicbt.setObjectName("musicbt")
        self.musicbt.setFont(QtGui.QFont("SansSerif",12))
        self.quitbt = QtWidgets.QPushButton(self.centralwidget)
        self.quitbt.setGeometry(QtCore.QRect(10, 450, 91, 31))
        self.quitbt.setObjectName("quitbt")
        self.quitbt.setFont(QtGui.QFont("SansSerif",12))
        self.helpbt = QtWidgets.QPushButton(self.centralwidget)
        self.helpbt.setGeometry(QtCore.QRect(10, 510, 91, 31))
        self.helpbt.setObjectName("quitbt")
        self.helpbt .setFont(QtGui.QFont("SansSerif",12))


        self.scr1 = QtWidgets.QListWidget(self.centralwidget)
        self.scr1.setStyleSheet('background-color: rgb(230,230,230);')
        self.scr1.setGeometry(QtCore.QRect(220, 120, 181, 201))
        self.scr1.setObjectName("playlist")



        self.scr1.setObjectName("scr1")
        #self.scrollAreaWidgetContents = QtWidgets.QWidget()
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 199))
        #self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        #self.scr1.setWidget(self.scrollAreaWidgetContents)


        self.scr1_2 = QtWidgets.QListWidget(self.centralwidget)
        self.scr1_2.setStyleSheet('background-color: rgb(230,230,230);')
        self.scr1_2.setGeometry(QtCore.QRect(490, 120, 181, 201))
        self.scr1_2.setObjectName("mixlist")
        #self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        #self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 179, 199))
       #self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        #self.scr1_2.setWidget(self.scrollAreaWidgetContents_2)



        self.choosebt = QtWidgets.QPushButton(self.centralwidget)
        self.choosebt.setGeometry(QtCore.QRect(220, 370, 50, 50))
        self.choosebt.setObjectName("choosebt")
        self.choosebt.setIcon(QtGui.QIcon(r'stop-button-512.png'))
        self.choosebt.setIconSize(QtCore.QSize(35,35))
        self.listenbt = QtWidgets.QPushButton(self.centralwidget)
        self.listenbt.setGeometry(QtCore.QRect(220, 440, 50, 50))
        self.listenbt.setObjectName("listenbt")
        self.listenbt.setIcon(QtGui.QIcon(r'play.png'))
        self.listenbt.setIconSize(QtCore.QSize(35,35))
        self.addbt = QtWidgets.QPushButton(self.centralwidget)
        self.addbt.setGeometry(QtCore.QRect(340, 370, 91, 31))
        self.addbt.setObjectName("addbt")
        self.addbt.setFont(QtGui.QFont("SansSerif",12))
        self.deletebt = QtWidgets.QPushButton(self.centralwidget)
        self.deletebt.setGeometry(QtCore.QRect(340, 510, 91, 31))
        self.deletebt.setObjectName("deletebt")
        self.deletebt.setFont(QtGui.QFont("SansSerif",12))
        self.savebt = QtWidgets.QPushButton(self.centralwidget)
        self.savebt.setGeometry(QtCore.QRect(450, 370, 91, 31))
        self.savebt.setObjectName("savebt")
        self.savebt.setFont(QtGui.QFont("SansSerif",12))
        self.pausebt = QtWidgets.QPushButton(self.centralwidget)
        self.pausebt.setGeometry(QtCore.QRect(220, 510, 50, 50))
        self.pausebt.setObjectName("pausebt")
        self.pausebt.setIcon(QtGui.QIcon(r'pause.png'))
        self.pausebt.setIconSize(QtCore.QSize(35,35))
        MainWindow.setCentralWidget(self.centralwidget)
        self.volumebt1 = QtWidgets.QPushButton(self.centralwidget)
        self.volumebt1.setGeometry(QtCore.QRect(580, 370, 60, 60))
        self.volumebt1.setObjectName("volumebt1")
        self.volumebt1.setIcon(QtGui.QIcon(r'volume up.png'))
        self.volumebt1.setIconSize(QtCore.QSize(50,50))
        self.volumebt2 = QtWidgets.QPushButton(self.centralwidget)
        self.volumebt2.setGeometry(QtCore.QRect(580, 480, 60, 60))
        self.volumebt2.setObjectName("volumebt2")
        self.volumebt2.setIcon(QtGui.QIcon(r'volume down.png'))
        self.volumebt2.setIconSize(QtCore.QSize(50,50))
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.play2bt = QtWidgets.QPushButton(self.centralwidget)
        self.play2bt.setGeometry(QtCore.QRect(340, 440, 91, 31))
        self.play2bt.setObjectName("play2bt")
        self.play2bt.setFont(QtGui.QFont("SansSerif",12))
        MainWindow.setStatusBar(self.statusbar)
        self.resetbt = QtWidgets.QPushButton(self.centralwidget)
        self.resetbt.setGeometry(QtCore.QRect(650, 10, 91, 31))
        self.resetbt.setObjectName("resetbt")
        self.resetbt.setFont(QtGui.QFont("SansSerif",12))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rockbt.setText(_translate("MainWindow", "Rock"))
        self.popbt.setText(_translate("MainWindow", "Pop"))
        self.countrybt.setText(_translate("MainWindow", "Country"))
        self.jazzbt.setText(_translate("MainWindow", "Jazz"))
        self.classicalbt.setText(_translate("MainWindow", "Classical"))
        self.bluesbt.setText(_translate("MainWindow", "Blues"))
        self.lb1.setText(_translate("MainWindow", "Choose genre"))
        self.lb2.setText(_translate("MainWindow", "Choose tempo"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.bpm60.setText(_translate("MainWindow", "60 BPM"))
        self.bpm120.setText(_translate("MainWindow", "120 BPM"))
        self.bpm180.setText(_translate("MainWindow", "180 BPM"))
        self.choosebt.setText(_translate("MainWindow", ""))
        self.listenbt.setText(_translate("MainWindow", ""))
        self.addbt.setText(_translate("MainWindow", "Add track"))
        self.deletebt.setText(_translate("MainWindow", "Delete"))
        self.savebt.setText(_translate("MainWindow", "Save"))
        self.pausebt.setText(_translate("MainWindow", ""))
        self.musicbt.setText(_translate("MainWindow", "Find music"))
        self.quitbt.setText(_translate("MainWindow", "Quit"))
        self.play2bt.setText(_translate("MainWindow", "Play music"))
        self.helpbt.setText(_translate("MainWindow", "Help"))
        self.volumebt1.setText(_translate("MainWindow", ""))
        self.volumebt2.setText(_translate("MainWindow", ""))
        self.name1.setText(_translate("MainWindow", "Playlist"))
        self.name2.setText(_translate("MainWindow", "Chosen music"))
        self.resetbt.setText(_translate("MainWindow", "Reset"))




class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       # oImage = QImage(r"background.jpg")
        #sImage = oImage.scaled(QSize(300,200))
       #palette = QPalette()
        #palette.setBrush(10, QBrush(sImage))
        #self.setPalette(palette)
        #self.w2 = Ui_SecondWindow()
        #self.w2.setupUi(self)

        path = os.getcwd()+'\\sound1.mp3'
        mixer.init()
        #Бинд кнопок
        self.ui.tempo.buttonClicked.connect(self.tempo)
        self.ui.genre.buttonClicked.connect(self.genre)
        #self.ui.searchlist.currentTextChanged.connect(self.getfiles)
        #self.ui.listWidget_2.currentTextChanged.connect(self.playmusic)
        self.ui.listenbt.clicked.connect(self.playmusic)
        self.ui.play2bt.clicked.connect(self.playmusic2)
        self.ui.addbt.clicked.connect(self.addmusic)
        self.ui.choosebt.clicked.connect(self.stopmusic)
        self.ui.savebt.clicked.connect(self.mix)
        self.ui.deletebt.clicked.connect(self.delete)
        self.ui.pausebt.clicked.connect(self.pause)
        self.ui.helpbt.clicked.connect(self.help)
        self.ui.volumebt1.clicked.connect(self.volume1)
        self.ui.volumebt2.clicked.connect(self.volume2)
        self.ui.musicbt.clicked.connect(self.findmusic)
        self.ui.resetbt.clicked.connect(self.reset)
        self.ui.quitbt.clicked.connect(self.close)
        #self.ui.fastBtn.clicked.connect(self.faster)
        #self.ui.slowBtn.clicked.connect(self.slowly)

        self.songs=[]#массив для проигрываемой музыки
        self.mixer=[]#массив для музыки из второго listboxа
        self.flag=0
        self.paused = False
        self.ganr = ''
        self.temp = ''
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol + 0.1)
        gromkost = str(int((vol+0.1)*10))
        self.ui.volumelb.setText(gromkost)

        #self.scandisk()

    def getsongs(self):
        try:
            if self.ganr != '' and self.temp != '':
                self.songs=[]
                self.ui.scr1.clear()

                path = os.path.join(os.getcwd(), self.ganr, self.temp)#путь, в котором мы находимся + жанр + темп
                try:
                    for files in os.listdir(path):

                        if files.endswith ('wav'):
                            self.songs.append(path + '\\'+ files)#добавляем песни с путем в массив
                            self.ui.scr1.addItem(files.strip())#добавляем названия песен в listbox
                            #self.songs.append()
                except Exception as e:
                    pass
                    #print(e)

        except Exception as e:
            #print(e)
            pass
    def tempo(self,button):
        self.temp = button.text()

        self.getsongs()

    def genre(self,button2):
        self.ganr = button2.text()
        self.getsongs()


    def scandisk(self):
        try:
            self.mode='mp3'
            mas=[]
            mas2=[]
            p=str(self.ui.lineEdit.text()).strip()
            file = codecs.open(u''+os.getcwd()+'\\dir.txt', "w", "utf-8")
            file.write(p)
            file.close()

            for rootdir, dirs, files in os.walk(str(p)):
                for file in files:
                    if((file.split('.')[-1])=='wav'):
                        mas.append(os.path.join(rootdir, file))
                        mas2.append(os.path.join(rootdir, file).split('\\')[-2])
            mas2 = dict(zip(mas2, mas2)).values()
            self.mp3=mas
            self.ui.searchlist.clear()
            for x in mas2:
                self.ui.searchlist.addItem(x.strip())
        except Exception as e:
            #print(e)
            pass


    def getfiles(self):
        try:
            self.flag=1
            self.mode='song'
            self.songs=[]
            self.ui.playlist.clear()
            catname=self.ui.searchlist.currentItem().text()
            for x in self.mp3:
                mp3=x.split('\\')[-2]
                if(catname==mp3.strip()):
                    self.songs.append(x)
                    self.ui.playlist.addItem(x.split('\\')[-1])
            self.ui.playlist.setFocus()
            self.flag=0
        except Exception as e:
            #print(e)
            pass


    def playmusic(self):
        if(self.flag==0):
            try:
                self.ui.label.setText("Welcome")
                selitem=self.ui.scr1.currentRow()#получаем индекс выбранной песни в listbox1
                put=self.songs[selitem] #текущая песня(выбранная)

                mixer.music.stop()
                mixer.music.load(u''+put)
                mixer.music.play()
                self.paused = False#обнуляем паузу
                self.ui.label.setText("Music is playing")

            except IndexError as e:
                self.ui.label.setText("Choose music or see help!")

    def playmusic2(self):
        try:
            if(self.flag==0):
                selitem=self.ui.scr1_2.currentRow()#получаем индекс выбранной песни в listbox1
                put=self.mixer[selitem]
                mixer.music.stop()
                mixer.music.load(u''+put)
                mixer.music.play()
                self.paused = False#обнуляем паузу
        except IndexError:
            self.ui.label.setText("Choose music or see help!")


    def addmusic(self):

        if(self.flag==0):
            try:
                selitem=self.ui.scr1.currentRow()#получаем индекс выбранной песни в listbox1
                put=self.songs[selitem]#выбираем песню с путем по индексу, полученному выше
                self.mixer.append(put)#записываем в массив listbox 2
                self.ui.scr1_2.addItem(put.split('\\')[-1])#записываем только название песни во второй listbox
            except IndexError:
                self.ui.label.setText("Choose music or see help!")

    def mix(self):
        if(self.flag==0):#чтобы не созраняли пустую песню
            try:
                if len(self.mixer) < 2:
                    self.ui.label.setText("Add at least two songs to the chosen music list")
                else:
                    path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
                    newname, okBtnPressed = QInputDialog.getText(self, 'Введите название для песни','Как хотите ее назвать?')#создаем диаологовое окно для называния песни
                    if okBtnPressed is False:
                        newname = 'song'
                    output = AudioSegment.from_wav(self.mixer[0])
                    for i in range(1,len(self.mixer)):
                        sound1 = AudioSegment.from_wav(self.mixer[1])

                        output= output.append(sound1)
                    output.export(path+newname+'.wav',format = "wav")
            except Exception as e:
                #print(e)
                pass
    def delete(self):
        try:
            self.flag=1
            self.mode='song'
            self.mixer=[]
            self.ui.scr1_2.clear()
            self.ui.scr1_2.setFocus()
            self.flag=0#
        except Exception as e:
            #print(e)
            pass

    def stopmusic(self):
        try:
            mixer.music.stop()
            self.ui.label.setText("Music is stopped")
        except Exception as e:
            #print(e)
            pass

    def reset(self):
        self.ui.genre.setExclusive(False)
        self.ui.tempo.setExclusive(False)
        self.ui.rockbt.setChecked(False)
        self.ui.bluesbt.setChecked(False)
        self.ui.classicalbt.setChecked(False)
        self.ui.popbt.setChecked(False)
        self.ui.countrybt.setChecked(False)
        self.ui.jazzbt.setChecked(False)

        self.ui.bpm60.setChecked(False)
        self.ui.bpm120.setChecked(False)
        self.ui.bpm180.setChecked(False)


        self.ui.genre.setExclusive(True)
        self.ui.tempo.setExclusive(True)


        self.songs=[]
        self.ui.scr1.clear()
        self.ui.scr1.setFocus()
        self.ganr = ''
        self.temp = ''

    def pause(self):
        if self.paused == True:
            mixer.music.unpause()
            self.ui.label.setText("Music is playing")
            self.paused = False
        elif self.paused == False:
            mixer.music.pause()
            self.ui.label.setText("Music is paused")
            self.paused = True

    def internet(self):
        try:
            QMessageBox.question(self,'internet', 'https://www.youtube.com/watch?v=QT8I_eUM-Ns', QMessageBox.Ok)
        except Exception as e:
            #print(e)
            pass



    def help(self):
        try:
            #textboxValue = self.textbox.text()
            #window = QMessageBox.question(self, 'Справка', "Чтобы выбрать музыку, выберите и жанр, и темп", QMessageBox.Ok)

            QMessageBox.question(self, 'Help',
"""- Чтобы выбрать нужный аудиофайл, выберите жанр и темп
- Чтобы сохранить Вашу песню,нажмите кнопку Save и выберите папку, где будет хранится песня
- Чтобы управлять музыкой из первого плейлиста, используйте кнопки "Стоп", "Пауза" и "Играть"
- Чтобы послушать музыку из второго плейлиста, используйте кнопки "Play music"
- Чтобы добавить музыку из первого плейлиста во второй, нажмите "Add music"
- Чтобы удалить песню из плейлиста нажмите "Delete"
- Чтобы выбрать аудиофайл из другой папки, нажмите "Find music"
- Чтобы обновить фильтр нажмите "Reset"



"""

                                 , QMessageBox.Ok)
        except Exception as e:
            #print(e)
            pass

    def findmusic(self):
        path = str(QFileDialog.getExistingDirectory(self, "Find music"))
        self.songs=[]
        self.ui.scr1.clear()
        try:
            for files in os.listdir(path):

                if files.endswith ('wav'):
                    self.songs.append(path + '\\'+ files)#добавляем песни с путем в массив
                    self.ui.scr1.addItem(files.strip())#добавляем названия песен в listbox
                    #self.songs.append()
        except Exception as e:
            #print(e)
            pass



    def close(self):

        reply = QMessageBox.question(self, 'Message', "Вы точно хотите выйти?",
        QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            uic.loadUi('goodbye.ui',self)
        else:
            pass

    def volume1(self):
        try:
            vol = mixer.music.get_volume()
            mixer.music.set_volume(vol + 0.1)
            if int((vol+0.1)*10) > 10:
                self.ui.volumelb.setText(str(10))
            else:
                gromkost = str(int((vol+0.1)*10))
                self.ui.volumelb.setText(gromkost)
        except Exception as e:
            #print(e)
            pass
    def volume2(self):
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol - 0.1)
        gromkost = str(int((vol - 0.1)*10))
        self.ui.volumelb.setText(gromkost)




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
