# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\zhouxuan.WLF\CloudSync\Scripts\video-processing\CGTeamWorkTool\CGTeamWorkTool.ui'
#
# Created: Tue Jun 06 18:09:36 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.serverEdit = QtGui.QLineEdit(self.centralwidget)
        self.serverEdit.setObjectName("serverEdit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.serverEdit)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.destEdit = QtGui.QLineEdit(self.centralwidget)
        self.destEdit.setObjectName("destEdit")
        self.horizontalLayout_3.addWidget(self.destEdit)
        self.destButton = QtGui.QPushButton(self.centralwidget)
        self.destButton.setObjectName("destButton")
        self.horizontalLayout_3.addWidget(self.destButton)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.shotPrefixEdit = QtGui.QLineEdit(self.centralwidget)
        self.shotPrefixEdit.setObjectName("shotPrefixEdit")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.shotPrefixEdit)
        self.databaseEdit = QtGui.QLineEdit(self.centralwidget)
        self.databaseEdit.setObjectName("databaseEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.databaseEdit)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.moduleEdit = QtGui.QLineEdit(self.centralwidget)
        self.moduleEdit.setObjectName("moduleEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.moduleEdit)
        self.pipelineEdit = QtGui.QLineEdit(self.centralwidget)
        self.pipelineEdit.setObjectName("pipelineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pipelineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.downloadButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.verticalLayout.addWidget(self.downloadButton)
        self.versionLabel = QtGui.QLabel(self.centralwidget)
        self.versionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CGTeamWork提交文件批量下载", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "流程", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "服务器路径", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "下载至", None, QtGui.QApplication.UnicodeUTF8))
        self.destButton.setText(QtGui.QApplication.translate("MainWindow", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "镜头前缀", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "项目数据库名", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "数据库模块名", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadButton.setText(QtGui.QApplication.translate("MainWindow", "下载提交的文件", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

