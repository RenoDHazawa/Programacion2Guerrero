# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Democreatetable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 404)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.verticalLayout_2.addWidget(self.lineEditDBName)
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.verticalLayout_2.addWidget(self.lineEditTableName)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEditColumnName = QtWidgets.QLineEdit(Dialog)
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.verticalLayout_3.addWidget(self.lineEditColumnName)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.comboBoxDataType = QtWidgets.QComboBox(Dialog)
        self.comboBoxDataType.setObjectName("comboBoxDataType")
        self.verticalLayout_4.addWidget(self.comboBoxDataType)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.pushButtonAddColumn = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddColumn.setMinimumSize(QtCore.QSize(0, 150))
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")
        self.horizontalLayout_2.addWidget(self.pushButtonAddColumn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.pushButtonCreateTable = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")
        self.verticalLayout_5.addWidget(self.pushButtonCreateTable)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setMaximumSize(QtCore.QSize(16777215, 200))
        self.labelResponse.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout_5.addWidget(self.labelResponse)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mi primera base de datos"))
        self.label.setText(_translate("Dialog", "Ingresar nombre de la base de datos"))
        self.label_5.setText(_translate("Dialog", "Ingresar nombre de tabla"))
        self.label_2.setText(_translate("Dialog", "Nombre de Columna"))
        self.label_3.setText(_translate("Dialog", "Tipo de data"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Agregar columna"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Crear tabla"))

