import sys
from GetStationsDurations import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Icons/Underground.resize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        ### Central Widget ###
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Images/Icons
        self.UndergroundImage = QtWidgets.QLabel(self.centralwidget)
        self.UndergroundImage.setGeometry(QtCore.QRect(300, 0, 200, 200))
        self.UndergroundImage.setText("")
        self.UndergroundImage.setPixmap(QtGui.QPixmap("./Icons/Underground.resize.png"))
        self.UndergroundImage.setObjectName("UndergroundImage")

        self.WorkAddressIcon = QtWidgets.QLabel(self.centralwidget)
        self.WorkAddressIcon.setGeometry(QtCore.QRect(240, 210, 48, 48))
        self.WorkAddressIcon.setAutoFillBackground(False)
        self.WorkAddressIcon.setText("")
        self.WorkAddressIcon.setPixmap(QtGui.QPixmap("./Icons/WorkAddressIcon.resize.png"))
        self.WorkAddressIcon.setScaledContents(False)
        self.WorkAddressIcon.setObjectName("WorkAddressIcon")

        self.MinClockIcon = QtWidgets.QLabel(self.centralwidget)
        self.MinClockIcon.setGeometry(QtCore.QRect(240, 290, 48, 48))
        self.MinClockIcon.setAutoFillBackground(False)
        self.MinClockIcon.setText("")
        self.MinClockIcon.setPixmap(QtGui.QPixmap("./Icons/ClockIcon.resize.png"))
        self.MinClockIcon.setScaledContents(False)
        self.MinClockIcon.setObjectName("MinClockIcon")

        self.MaxClockIcon = QtWidgets.QLabel(self.centralwidget)
        self.MaxClockIcon.setGeometry(QtCore.QRect(240, 370, 48, 48))
        self.MaxClockIcon.setAutoFillBackground(False)
        self.MaxClockIcon.setText("")
        self.MaxClockIcon.setPixmap(QtGui.QPixmap("./Icons/ClockIcon.resize.png"))
        self.MaxClockIcon.setScaledContents(False)
        self.MaxClockIcon.setObjectName("MaxClockIcon")

        # User inputs 
        self.Postcode = QtWidgets.QLineEdit(self.centralwidget)
        self.Postcode.setGeometry(QtCore.QRect(310, 220, 181, 30))
        self.Postcode.setObjectName("Postcode")

        self.MinDuration = QtWidgets.QLineEdit(self.centralwidget)
        self.MinDuration.setGeometry(QtCore.QRect(310, 300, 181, 30))
        self.MinDuration.setObjectName("MinDuration")

        self.MaxDuration = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxDuration.setGeometry(QtCore.QRect(310, 380, 181, 30))
        self.MaxDuration.setObjectName("MaxDuration")

        # Run button
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(600, 500, 50, 30))
        self.Run.setObjectName("Run")
        self.Run.clicked.connect(self.button_click)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(310, 250, 200, 16))
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(310, 330, 200, 16))
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(310, 410, 200, 16))
        self.label3.setObjectName("label3")

        self.loadingGif = QtWidgets.QLabel(self.centralwidget)
        self.loadingGif.setGeometry(QtCore.QRect(300, 490, 200, 50))
        self.loadingGif.setObjectName("loadingGif")

        self.movie = QtGui.QMovie("./Icons/Loading.resize.gif")
        self.loadingGif.setMovie(self.movie)
        self.movie.start()

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Find Possible Stations"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.label1.setText(_translate("MainWindow", "Enter Work Postcode"))
        self.label2.setText(_translate("MainWindow", "Enter Minimum Commute Duration"))
        self.label3.setText(_translate("MainWindow", "Enter Maximum Commute Duration"))

    def button_click(self):
        office_postcode = self.Postcode.text()
        min_duration = self.MinDuration.text()
        max_duration = self.MaxDuration.text()

        if office_postcode == "":
            print("Postcode must not be empty")
        if min_duration == "":
            min_duration = 0
        if max_duration == "":
            max_duration = sys.maxsize

        if office_postcode != "":
            try:
                duration_dict = find_duration_from_station(office_postcode)
                print()
                print("POSSIBLE STATIONS:")
                print()
                for key, value in duration_dict.items():
                    if value >= int(min_duration) and value <= int(max_duration):
                        print(key, ":", value)
            except: 
                print("An exception occured")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
