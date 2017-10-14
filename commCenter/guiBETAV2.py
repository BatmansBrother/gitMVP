# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiPractice1_4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
from time import strftime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1202, 868)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 118, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(98, 98, 98))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sessionFrame = QtGui.QFrame(self.centralwidget)
        self.sessionFrame.setMinimumSize(QtCore.QSize(166, 673))
        self.sessionFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sessionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sessionFrame.setObjectName(_fromUtf8("sessionFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.sessionFrame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.sessionLabel = QtGui.QLabel(self.sessionFrame)
        self.sessionLabel.setMaximumSize(QtCore.QSize(60, 17))
        self.sessionLabel.setObjectName(_fromUtf8("sessionLabel"))
        self.verticalLayout_3.addWidget(self.sessionLabel, QtCore.Qt.AlignHCenter)
        self.sessionText = QtGui.QTextEdit(self.sessionFrame)
        self.sessionText.setObjectName(_fromUtf8("sessionText"))
        self.sessionText._update_timer = QtCore.QTimer()					#added
        self.sessionText._update_timer.timeout.connect(self.update_label)	#added
        self.sessionText._update_timer.start(500) # milliseconds				#added

        self.verticalLayout_3.addWidget(self.sessionText)
        self.gridLayout.addWidget(self.sessionFrame, 2, 2, 2, 1)
        self.picButtonFrame = QtGui.QFrame(self.centralwidget)
        self.picButtonFrame.setMaximumSize(QtCore.QSize(820, 47))
        self.picButtonFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.picButtonFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.picButtonFrame.setObjectName(_fromUtf8("picButtonFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.picButtonFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pic1Button = QtGui.QPushButton(self.picButtonFrame)
        self.pic1Button.setObjectName(_fromUtf8("pic1Button"))
        self.horizontalLayout.addWidget(self.pic1Button)
        self.pic2Button = QtGui.QPushButton(self.picButtonFrame)
        self.pic2Button.setObjectName(_fromUtf8("pic2Button"))
        self.horizontalLayout.addWidget(self.pic2Button)
        self.pic3Button = QtGui.QPushButton(self.picButtonFrame)
        self.pic3Button.setObjectName(_fromUtf8("pic3Button"))
        self.horizontalLayout.addWidget(self.pic3Button)
        self.gridLayout.addWidget(self.picButtonFrame, 3, 1, 1, 1)
        self.hexLabel = QtGui.QLabel(self.centralwidget)
        self.hexLabel.setText(_fromUtf8(""))
        self.hexLabel.setPixmap(QtGui.QPixmap(_fromUtf8("/home/carson/gitMVP/commCenter/images/hexlogo4.png")))
        self.hexLabel.setObjectName(_fromUtf8("hexLabel"))
        self.gridLayout.addWidget(self.hexLabel, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressBar.setPalette(palette)
        self.progressBar.setAutoFillBackground(False)
######################################################################################################################################
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar._update_timer = QtCore.QTimer()					#added
        self.progressBar._update_timer.timeout.connect(self.update_progress)	#added
        self.progressBar._update_timer.start(1000) # milliseconds
		

        self.gridLayout.addWidget(self.progressBar, 4, 1, 1, 1)
        self.logButton = QtGui.QPushButton(self.centralwidget)
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.gridLayout.addWidget(self.logButton, 4, 2, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mobileFrame = QtGui.QFrame(self.frame)
        self.mobileFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mobileFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mobileFrame.setObjectName(_fromUtf8("mobileFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mobileFrame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mobileLabel = QtGui.QLabel(self.mobileFrame)
        self.mobileLabel.setObjectName(_fromUtf8("mobileLabel"))
        self.verticalLayout_2.addWidget(self.mobileLabel, QtCore.Qt.AlignHCenter)
        self.mobileText = QtGui.QTextEdit(self.mobileFrame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.mobileText.setPalette(palette)
        self.mobileText.setObjectName(_fromUtf8("mobileText"))
        self.mobileText._update_timer = QtCore.QTimer()							#added
        self.mobileText._update_timer.timeout.connect(self.update_label)		#added
        self.mobileText._update_timer.start(500) # milliseconds					#added

        self.verticalLayout_2.addWidget(self.mobileText)
        self.verticalLayout.addWidget(self.mobileFrame)
        self.encoderFrame = QtGui.QFrame(self.frame)
        self.encoderFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.encoderFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.encoderFrame.setObjectName(_fromUtf8("encoderFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.encoderFrame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.encoderLabel = QtGui.QLabel(self.encoderFrame)
        self.encoderLabel.setObjectName(_fromUtf8("encoderLabel"))
        self.verticalLayout_4.addWidget(self.encoderLabel, QtCore.Qt.AlignHCenter)
        self.encodersText = QtGui.QTextEdit(self.encoderFrame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(41, 227, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 227, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.encodersText.setPalette(palette)
        self.encodersText.setObjectName(_fromUtf8("encodersText"))
        self.encodersText._update_timer = QtCore.QTimer()						#added
        self.encodersText._update_timer.timeout.connect(self.update_label)		#added
        self.encodersText._update_timer.start(500) # milliseconds				#added


        self.verticalLayout_4.addWidget(self.encodersText)
        self.verticalLayout.addWidget(self.encoderFrame)
        self.serverFrame = QtGui.QFrame(self.frame)
        self.serverFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.serverFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.serverFrame.setObjectName(_fromUtf8("serverFrame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.serverFrame)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.serverLabel = QtGui.QLabel(self.serverFrame)
        self.serverLabel.setObjectName(_fromUtf8("serverLabel"))
        self.verticalLayout_5.addWidget(self.serverLabel, QtCore.Qt.AlignHCenter)
        self.serverText = QtGui.QTextEdit(self.serverFrame)
        self.serverText.setMinimumSize(QtCore.QSize(146, 259))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.serverText.setPalette(palette)
        self.serverText.setObjectName(_fromUtf8("serverText"))
        self.serverText._update_timer = QtCore.QTimer()					#added
        self.serverText._update_timer.timeout.connect(self.update_label)	#added
        self.serverText._update_timer.start(500) # milliseconds				#added

        self.verticalLayout_5.addWidget(self.serverText)
        self.verticalLayout.addWidget(self.serverFrame)
        self.gridLayout.addWidget(self.frame, 1, 0, 4, 1)
        self.picFrame = QtGui.QFrame(self.centralwidget)
        self.picFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.picFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.picFrame.setObjectName(_fromUtf8("picFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.picFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        

        ########################

        self.pic1Label = QtGui.QLabel(self.picFrame)
        self.pic1Label.setText(_fromUtf8(""))
        self.pic1Label.setPixmap(QtGui.QPixmap(_fromUtf8("/home/carson/gitMVP/commCenter/images/cat.jpg")))
        self.pic1Label.setObjectName(_fromUtf8("pic1Label"))

        
        self.pic2Label = QtGui.QLabel(self.picFrame)                                                        #Addedd
        self.pic2Label.setText(_fromUtf8(""))																#added
        self.pic2Label.setPixmap(QtGui.QPixmap(_fromUtf8("/home/carson/gitMVP/commCenter/images/coursePlot.jpeg")))				#added
        self.pic2Label.setObjectName(_fromUtf8("pic2Label"))                                                #added
        

        self.pic3Label = QtGui.QLabel(self.picFrame)                                                        #Addedd
        self.pic3Label.setText(_fromUtf8(""))																#added
        self.pic3Label.setPixmap(QtGui.QPixmap(_fromUtf8("/home/carson/gitMVP/commCenter/images/shroom.jpg")))				#added
        self.pic3Label.setObjectName(_fromUtf8("pic3Label")) 
        
        ###########################   

        self.gridLayout_2.addWidget(self.pic1Label, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.pic2Label, 1, 0, 1, 1)												#added
        self.gridLayout_2.addWidget(self.pic3Label, 1, 0, 1, 1)
        
        self.picDescripFrame = QtGui.QFrame(self.picFrame)
        self.picDescripFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.picDescripFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.picDescripFrame.setObjectName(_fromUtf8("picDescripFrame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.picDescripFrame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.picture1descriptionLabel = QtGui.QLabel(self.picDescripFrame)
        self.picture1descriptionLabel.hide()
        self.picture1descriptionLabel.setObjectName(_fromUtf8("picture1descriptionLabel"))
        self.horizontalLayout_3.addWidget(self.picture1descriptionLabel, QtCore.Qt.AlignHCenter)

        self.picture2descriptionLabel = QtGui.QLabel(self.picDescripFrame)
        self.picture2descriptionLabel.hide()
        self.picture2descriptionLabel.setObjectName(_fromUtf8("picture2descriptionLabel"))
        self.horizontalLayout_3.addWidget(self.picture2descriptionLabel, QtCore.Qt.AlignHCenter)

        self.picture3descriptionLabel = QtGui.QLabel(self.picDescripFrame)
        self.picture3descriptionLabel.hide()
        self.picture3descriptionLabel.setObjectName(_fromUtf8("picture3descriptionLabel"))
        self.horizontalLayout_3.addWidget(self.picture3descriptionLabel, QtCore.Qt.AlignHCenter)

        self.gridLayout_2.addWidget(self.picDescripFrame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.picFrame, 1, 1, 2, 1)
        self.ledFrame = QtGui.QFrame(self.centralwidget)
        self.ledFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ledFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.ledFrame.setObjectName(_fromUtf8("ledFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.ledFrame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ledLabel = QtGui.QLabel(self.ledFrame)
        self.ledLabel.setText(_fromUtf8(""))
        self.ledLabel.setPixmap(QtGui.QPixmap(_fromUtf8("/home/carson/gitMVP/commCenter/images/LEDgreenScaled.png")))
        self.ledLabel.setObjectName(_fromUtf8("ledLabel"))
        self.horizontalLayout_2.addWidget(self.ledLabel)
        self.gridLayout.addWidget(self.ledFrame, 1, 2, 1, 1)
        self.ledFrame.setMaximumSize(QtCore.QSize(351, 50))

        #self.lcd = QtGui.QFrame(self.centralwidget)
        #self.lcd._update_timer = QtCore.QTimer()                 #added
        #self.lcd._update_timer.timeout.connect(self.Time)    #added
        #self.lcd._update_timer.start(500) # milliseconds
        #self.gridLayout.addWidget(self.lcd, 0, 2, 1, 1)

      
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.gridLayout.addWidget(self.timeEdit, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pic3Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic1Label.hide)
        QtCore.QObject.connect(self.pic3Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic2Label.hide)
        QtCore.QObject.connect(self.pic3Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic3Label.show) 
        QtCore.QObject.connect(self.pic2Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic1Label.hide)
        QtCore.QObject.connect(self.pic2Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic3Label.hide)
        QtCore.QObject.connect(self.pic2Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic2Label.show)                  #added
        QtCore.QObject.connect(self.pic1Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic2Label.hide)                  #added
        QtCore.QObject.connect(self.pic1Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic3Label.hide)
        QtCore.QObject.connect(self.pic1Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pic1Label.show)

        QtCore.QObject.connect(self.pic1Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture1descriptionLabel.show)
        QtCore.QObject.connect(self.pic1Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture2descriptionLabel.hide)
        QtCore.QObject.connect(self.pic1Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture3descriptionLabel.hide)

        QtCore.QObject.connect(self.pic2Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture2descriptionLabel.show)
        QtCore.QObject.connect(self.pic2Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture1descriptionLabel.hide)
        QtCore.QObject.connect(self.pic2Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture3descriptionLabel.hide)

        QtCore.QObject.connect(self.pic3Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture3descriptionLabel.show)
        QtCore.QObject.connect(self.pic3Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture1descriptionLabel.hide)
        QtCore.QObject.connect(self.pic3Button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.picture2descriptionLabel.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.sessionLabel.setText(_translate("MainWindow", "Seshion", None))
        self.sessionText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
        self.pic1Button.setText(_translate("MainWindow", "1", None))
        self.pic2Button.setText(_translate("MainWindow", "2", None))
        self.pic3Button.setText(_translate("MainWindow", "3", None))
        self.logButton.setText(_translate("MainWindow", "View Logs", None))
        self.mobileLabel.setText(_translate("MainWindow", "Mobile", None))
        self.mobileText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
        self.encoderLabel.setText(_translate("MainWindow", "Encoders", None))
        self.encodersText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
        self.serverLabel.setText(_translate("MainWindow", "Server", None))
        self.serverText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))
        self.picture1descriptionLabel.setText(_translate("MainWindow", "The Label for picture #1 will go here.", None))
        self.picture2descriptionLabel.setText(_translate("MainWindow", "The Label for picture #2 will go here.", None))
        self.picture3descriptionLabel.setText(_translate("MainWindow", "The Label for picture #3 will go here.", None))


    
    def update_label(self):
            global oldData
            global oldData2
            global oldData3
            global oldData4

            newData = open('/home/carson/gitMVP/commCenter/data/mobileData.txt').read()
            if oldData != newData:
                with open ("/home/carson/gitMVP/commCenter/data/mobileData.txt", "r") as myfile:
                    newData = myfile.read().replace('/n', '')
                oldData = newData
                self.mobileText.append(newData)
            #else:
                #return 0

            newData2 = open('/home/carson/gitMVP/commCenter/data/sessionData.txt').read()
            if oldData2 != newData2:
                with open ("/home/carson/gitMVP/commCenter/data/sessionData.txt", "r") as myfile:
                    newData2 = myfile.read().replace('/n', '')
                oldData2 = newData2
                self.sessionText.append(newData2)
            #else:
                #return 0

            newData3 = open('/home/carson/gitMVP/commCenter/data/encoderData.txt').read()
            if oldData3 != newData3:
                with open ("/home/carson/gitMVP/commCenter/data/encoderData.txt", "r") as myfile:
                    newData3 = myfile.read().replace('/n', '')
                oldData3 = newData3
                self.encodersText.append(newData3)
            #else:
                #return 0

            newData4 = open('/home/carson/gitMVP/commCenter/data/serverData.txt',"r")
            lineList = newData4.readlines()
            newData4.close()
            #print str(len(lineList)) + " old is" + str(oldData4)
            if (len(lineList) > oldData4):
                #with open ("/home/carson/gitMVP/commCenter/data/serverData.txt", "r") as myfile:
                #newData4 = myfile.read()
                with open ("/home/carson/gitMVP/commCenter/data/serverData.txt", "r") as myfile:
                    newData3 = myfile.read().replace('/n', '')
                oldData4 = len(lineList)
                #print " old is now" + str(oldData4)
                self.serverText.append(str(lineList[-1]))
            
        
    def update_progress(self):
            
            n = open('/home/carson/gitMVP/commCenter/data/progressBar.txt').read()
            
            self.progressBar.setProperty("value" , n)
            

    #def Time(self):
            #self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
        



import xz_rc

#if __name__ == "__main__":
def guiProc():
    import sys
    global oldData
    global oldData2
    global oldData3
    global oldData4
    oldData = ''	
    oldData2 = ''
    oldData3 = ''
    oldData4 = 0
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

