#mport tkinter
import PyQt5
#rom tkinter import messagebox
#rom tkinter import *

#op = tkinter.Tk()
import PyQt5.QtGui
#ef helloCallBack():
#   messagebox.showinfo( "Hello Python", "Hello World")

# = tkinter.Button(top, text ="Hello", command = helloCallBack)
#.pack()
#op.mainloop()



#op = Tk()
#1 = Label(top, text="User Name")
#1.pack( side = LEFT)
#1 = Entry(top, bd =5)

#1.pack(side = RIGHT)

#op.mainloop()
import sys
from PyQt4 import QtGui


def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle("maruthi")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()