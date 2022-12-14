# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usethis.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

'''much of the documentation of the code is at the bottom or in comments to mark where we've used lambda functions to comment buttons accordingly.
alot of the work was done trying to get the formula to behave corrently as well as getting the right lambda variables to line up correctly.
The GUI design turns out to be quite harder then normal, and this project actually gave quite a lot of learning in terms of how to set up GUIs for good UI's. '''

from PyQt5 import QtCore, QtGui, QtWidgets
'''imports for the pyqt5 function.'''

class Ui_MainWindow(object):
'''these are the elements generated by pyqt5.'''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.initialPrinciple_Lbl = QtWidgets.QLabel(self.centralwidget)
        self.initialPrinciple_Lbl.setGeometry(QtCore.QRect(40, 210, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.initialPrinciple_Lbl.setFont(font)
        self.initialPrinciple_Lbl.setObjectName("initialPrinciple_Lbl")
        self.results_Disp = QtWidgets.QLabel(self.centralwidget)
        self.results_Disp.setGeometry(QtCore.QRect(250, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.results_Disp.setFont(font)
        self.results_Disp.setWordWrap(True)
        self.results_Disp.setObjectName("results_Disp")
        self.annualRate_Lbl = QtWidgets.QLabel(self.centralwidget)
        self.annualRate_Lbl.setGeometry(QtCore.QRect(70, 240, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.annualRate_Lbl.setFont(font)
        self.annualRate_Lbl.setObjectName("annualRate_Lbl")
        self.compond_Lbl = QtWidgets.QLabel(self.centralwidget)
        self.compond_Lbl.setGeometry(QtCore.QRect(80, 310, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.compond_Lbl.setFont(font)
        self.compond_Lbl.setObjectName("compond_Lbl")
        self.time_Lbl = QtWidgets.QLabel(self.centralwidget)
        self.time_Lbl.setGeometry(QtCore.QRect(60, 270, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.time_Lbl.setFont(font)
        self.time_Lbl.setScaledContents(False)
        self.time_Lbl.setWordWrap(True)
        self.time_Lbl.setIndent(0)
        self.time_Lbl.setObjectName("time_Lbl")
        self.principle_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.principle_Input.setGeometry(QtCore.QRect(250, 210, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.principle_Input.setFont(font)
        self.principle_Input.setObjectName("principle_Input")
        self.rate_input = QtWidgets.QLineEdit(self.centralwidget)
        self.rate_input.setGeometry(QtCore.QRect(250, 240, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.rate_input.setFont(font)
        self.rate_input.setObjectName("rate_input")
        self.compound_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.compound_Input.setGeometry(QtCore.QRect(250, 270, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.compound_Input.setFont(font)
        self.compound_Input.setObjectName("compound_Input")
        self.quart_Rad = QtWidgets.QRadioButton(self.centralwidget)
        self.quart_Rad.setGeometry(QtCore.QRect(230, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.quart_Rad.setFont(font)
        self.quart_Rad.setObjectName("quart_Rad")
        self.annual_Rad = QtWidgets.QRadioButton(self.centralwidget)
        self.annual_Rad.setGeometry(QtCore.QRect(350, 310, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.annual_Rad.setFont(font)
        self.annual_Rad.setObjectName("annual_Rad")
        self.calc_Btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.calculateCompInt())
        '''this is where we impliment the lambda function for use in the calculate button of the program.'''
        self.calc_Btn.setGeometry(QtCore.QRect(120, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.calc_Btn.setFont(font)
        self.calc_Btn.setObjectName("calc_Btn")
        self.comp_Int_Calc_Lbl = QtWidgets.QLabel(self.centralwidget)
        self.comp_Int_Calc_Lbl.setGeometry(QtCore.QRect(40, 20, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(24)
        self.comp_Int_Calc_Lbl.setFont(font)
        self.comp_Int_Calc_Lbl.setObjectName("comp_Int_Calc_Lbl")
        self.formula_Pic = QtWidgets.QLabel(self.centralwidget)
        self.formula_Pic.setGeometry(QtCore.QRect(100, 80, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.formula_Pic.setFont(font)
        self.formula_Pic.setText("")
        self.formula_Pic.setPixmap(QtGui.QPixmap("../compIntCalc/compintpic.PNG"))
        self.formula_Pic.setObjectName("formula_Pic")
        self.results_Lbl = QtWidgets.QLabel(self.centralwidget)
        self.results_Lbl.setGeometry(QtCore.QRect(160, 410, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.results_Lbl.setFont(font)
        self.results_Lbl.setObjectName("results_Lbl")
        self.clear_Btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda : self.clearCompInt())
        '''anouther example of lambda in use on clicked. this one is for the clear button in the GUI.'''
        self.clear_Btn.setGeometry(QtCore.QRect(250, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.clear_Btn.setFont(font)
        self.clear_Btn.setObjectName("clear_Btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
       '''a lot of these are for label names, such as the initial principle, or the annual rate.'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.initialPrinciple_Lbl.setText(_translate("MainWindow", "Initial Principle (P): $"))
        self.results_Disp.setText(_translate("MainWindow", "Results here!"))
        self.annualRate_Lbl.setText(_translate("MainWindow", "Annual Rate (r): %"))
        self.compond_Lbl.setText(_translate("MainWindow", "Compound (n):"))
        self.time_Lbl.setText(_translate("MainWindow", "Time (t in years):"))
        self.quart_Rad.setText(_translate("MainWindow", "Quarterly"))
        self.annual_Rad.setText(_translate("MainWindow", "Annually"))
        self.calc_Btn.setText(_translate("MainWindow", "Calculate"))
        self.comp_Int_Calc_Lbl.setText(_translate("MainWindow", "Compound Interest Calculator"))
        self.results_Lbl.setText(_translate("MainWindow", "Result:"))
        self.clear_Btn.setText(_translate("MainWindow", "Clear"))

    def calculateCompInt(self):
        '''this is the function for the compound interest calculator.
        much of the variables in the function should be self explainitory.
        annual rate is divided by 100 to turn it into a percentage
        '''
        try:
            '''
            'p' is the initial principle
            'r' is the rate turing a whole int into a precentage.
            't' is time expressed in years. 
            'n' is expressed as the radial for compound.
            for the sake of math, 1 is considere once annually, and 4 is considered quarterly.  
            '''

            p = int(self.principle_Input.text())
            r = int(self.rate_input.text()) /100
            t = int(self.compound_Input.text())
            if self.annual_Rad.isChecked():
                n = 1
            else:
                n = 4


            result = p * (1 + (r / n)) ** (n * t)
            '''this was the one that took the most to configure.
            making sure the variables line up accordingly to make sure that the formula functions as intented
            rather then just numbers spitting out numbers can be lightly time consuming. Over all however this gave me a bit more confidence.'''
            self.results_Disp.setText(f"${result:.2f}")
        except:
            self.results_Disp.setText(f"Must be an Int.")

    def clearCompInt(self):
        '''clear function to clear the numbers if you're done calculating the numbers to the variables. '''
        self.principle_Input.setText("")
        self.rate_input.setText("")
        self.compound_Input.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
