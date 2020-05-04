# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(585, 311)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 255)")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.horizontalLayout.addWidget(self.lineEditDBName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonCreateDB = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")
        self.verticalLayout.addWidget(self.pushButtonCreateDB)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout.addWidget(self.labelResponse)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Ingrese el nombre de la base de datos"))
        self.pushButtonCreateDB.setText(_translate("Dialog", "PushButton"))

