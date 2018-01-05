

from PyQt5 import QtCore, QtGui, QtWidgets
import nltk
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem
from nltk.corpus import stopwords


class Ui_MainWindow(object):
    result=""
    i = 1
    sentence = ""
    j = 1
    sent_token = ""
    row=col=0
    wordopt=""
    word_s=[]
    word_np=[]
    word_pp=[]
    word_vp=[]

    def grammer(self):
        self.sentence = self.textEdit.toPlainText()

        #self.sentence = "maruthi is a good boy"
        print(self.sentence)

        grammar = r"""
          NP: {<DT|JJ.*|NN.*>+}          # Chunk sequences of DT, JJ, NN
          PP: {<IN><NP>}               # Chunk prepositions followed by NP
          VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
          """

        # [('it', 'PRP'), ('is', 'VBZ'), ('good', 'JJ'), ('but', 'CC'), ('not', 'RB'), ('bad', 'JJ')]

        self.sent_token = nltk.sent_tokenize(self.sentence)
        print(self.sent_token)
        for s in self.sent_token:
            print(s)
        stop = set(stopwords.words('english'))
        #print(stop)
        for sent in self.sent_token:
            word = nltk.word_tokenize(sent)
            print(nltk.pos_tag(word))
            #sort_word = [i for i in word if i not in stop]
            word_pos = nltk.pos_tag(word)
            print(word_pos)
            cp = nltk.RegexpParser(grammar)
            self.result = cp.parse(word_pos)
            for i in self.result.subtrees():
                print(i.label())
                word_st = i.leaves()
                self.wordopt = [r for r, pos in word_st if r not in stop]
                print(self.wordopt)
                if i.label() == "S":
                    for wor in self.wordopt:
                        self.word_s.append(wor)
                if i.label() == "NP":
                    for wor in self.wordopt:
                        self.word_np.append(wor)
                if i.label() == "VP":
                    for wor in self.wordopt:
                        self.word_vp.append(wor)
                if i.label() == "PP":
                    for wor in self.wordopt:
                        self.word_pp.append(wor)
            self.output()
            print(self.result)
            print(self.word_s)
            print(self.word_np)
            print(self.word_vp)
            self.result.draw()


    def addList(self):
        print(self.sentence)

        for sent in self.sent_token:
            addstr = str(self.i) + ". " + str(sent)
            self.listWidget_2.addItem(addstr)
            self.i = self.i + 1

    def delList(self):
        self.listWidget_2.takeItem(self.listWidget_2.currentRow())



    def output(self):
        table = self.tableWidget
        table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        table.setRowCount(self.row+2)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(('SENTENCE', 'NP', 'VP' ,'PP' ))
        self.row = self.row+1
        table.setItem(self.row - 1, 0, QTableWidgetItem(str(self.word_s)))
        table.setItem(self.row-1, 1, QTableWidgetItem(str(self.word_np)))
        table.setItem(self.row - 1, 2, QTableWidgetItem(str(self.word_vp)))
        table.setItem(self.row - 1, 3, QTableWidgetItem(str(self.word_pp)))
        table.resizeColumnsToContents()
        self.word_np=[]
        self.word_pp=[]
        self.word_s=[]
        self.word_vp=[]


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 1169)
        MainWindow.setSizeIncrement(QtCore.QSize(70, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setSizeIncrement(QtCore.QSize(5, 6))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setSizeIncrement(QtCore.QSize(5, 6))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFontWeight(30)
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.grammer)
        self.pushButton.clicked.connect(self.addList)
        self.pushButton_2.clicked.connect(self.delList)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Type text to classify</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Row added </span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "ADD SENTENCE"))
        self.pushButton_2.setText(_translate("MainWindow", "REMOVE SENTENCE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

