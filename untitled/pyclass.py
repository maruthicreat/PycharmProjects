# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyclass.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import nltk
from PyQt5 import QtCore, QtGui, QtWidgets
from nltk.corpus import stopwords




class Ui_MainWindow(object):
    def draw(self):
        sentence = self.textEdit.toPlainText()
        print(sentence)

        grammar = r"""
              NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
              PP: {<IN><NP>}               # Chunk prepositions followed by NP
              VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
              CLAUSE: {<NP><VP>}           # Chunk NP, VP
              """

        # [('it', 'PRP'), ('is', 'VBZ'), ('good', 'JJ'), ('but', 'CC'), ('not', 'RB'), ('bad', 'JJ')]

        sent_token = nltk.sent_tokenize(sentence)
        stop = set(stopwords.words('english'))
        print(stop)
        for sent in sent_token:
            print(sent)
            word = nltk.word_tokenize(sent)
            print(word)
            sort_word = [i for i in word if i not in stop]
            word_pos = nltk.pos_tag(sort_word)
            print(word_pos)
            cp = nltk.RegexpParser(grammar, loop=2)
            result = cp.parse(word_pos)
            print(result)
            result.draw()

    def hai(self):
        print("hai")
        login = self.textEdit.toPlainText()
        print(login)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 972)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setStatusTip("")
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        self.pushButtonOk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.gridLayout.addWidget(self.pushButtonOk, 1, 0, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 38))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPast = QtWidgets.QAction(MainWindow)
        self.actionPast.setObjectName("actionPast")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPast)
        self.menuEdit.addAction(self.actionUndo)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        #self.pushButtonOk.clicked.connect(self.textEdit.)
        #self.pushButtonOk.clicked.connect(self.textBrowser.paste)
        self.pushButtonOk.clicked.connect(self.draw)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\" bgcolor=\"#ffff00\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.pushButtonOk.setText(_translate("MainWindow", "ok"))
        self.pushButtonCancel.setText(_translate("MainWindow", "cancel"))
        self.menuFile.setTitle(_translate("MainWindow", "file"))
        self.menuEdit.setTitle(_translate("MainWindow", "edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "help"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCopy.setText(_translate("MainWindow", "copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPast.setText(_translate("MainWindow", "past"))
        self.actionPast.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionUndo.setText(_translate("MainWindow", "undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionAbout.setText(_translate("MainWindow", "about"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



