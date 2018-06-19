# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(40, 60))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.gridLayout = QtWidgets.QGridLayout(self.homeTab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.serviceNoLabel = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.serviceNoLabel.setFont(font)
        self.serviceNoLabel.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.serviceNoLabel.setObjectName("serviceNoLabel")
        self.gridLayout_3.addWidget(self.serviceNoLabel, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.homeTab)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)
        self.modeValuelabel = QtWidgets.QLabel(self.homeTab)
        self.modeValuelabel.setText("")
        self.modeValuelabel.setObjectName("modeValuelabel")
        self.gridLayout_3.addWidget(self.modeValuelabel, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.defaultTempValueLabel = QtWidgets.QLabel(self.homeTab)
        self.defaultTempValueLabel.setText("")
        self.defaultTempValueLabel.setObjectName("defaultTempValueLabel")
        self.gridLayout_3.addWidget(self.defaultTempValueLabel, 3, 1, 1, 1)
        self.rangeLabel = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.rangeLabel.setFont(font)
        self.rangeLabel.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.rangeLabel.setObjectName("rangeLabel")
        self.gridLayout_3.addWidget(self.rangeLabel, 1, 0, 1, 1)
        self.defaultTempLabel = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.defaultTempLabel.setFont(font)
        self.defaultTempLabel.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.defaultTempLabel.setObjectName("defaultTempLabel")
        self.gridLayout_3.addWidget(self.defaultTempLabel, 3, 0, 1, 1)
        self.modeLabel = QtWidgets.QLabel(self.homeTab)
        self.modeLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeLabel.sizePolicy().hasHeightForWidth())
        self.modeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.modeLabel.setFont(font)
        self.modeLabel.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.modeLabel.setObjectName("modeLabel")
        self.gridLayout_3.addWidget(self.modeLabel, 0, 0, 1, 1)
        self.serviceNoValueLabel = QtWidgets.QLabel(self.homeTab)
        self.serviceNoValueLabel.setText("")
        self.serviceNoValueLabel.setObjectName("serviceNoValueLabel")
        self.gridLayout_3.addWidget(self.serviceNoValueLabel, 2, 1, 1, 1)
        self.rangeValueLabel = QtWidgets.QLabel(self.homeTab)
        self.rangeValueLabel.setText("")
        self.rangeValueLabel.setObjectName("rangeValueLabel")
        self.gridLayout_3.addWidget(self.rangeValueLabel, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.detailtableWidget = QtWidgets.QTableWidget(self.homeTab)
        self.detailtableWidget.setObjectName("detailtableWidget")
        self.detailtableWidget.setColumnCount(9)
        self.detailtableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailtableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout_2.addWidget(self.detailtableWidget, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.homeTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.homeTab, icon, "")
        self.countTab = QtWidgets.QWidget()
        self.countTab.setObjectName("countTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.countTab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 3, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton = QtWidgets.QPushButton(self.countTab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.comboBox_6 = QtWidgets.QComboBox(self.countTab)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_2.addWidget(self.comboBox_6)
        self.label_13 = QtWidgets.QLabel(self.countTab)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox_5 = QtWidgets.QComboBox(self.countTab)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_2.addWidget(self.comboBox_5)
        self.label_18 = QtWidgets.QLabel(self.countTab)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.comboBox_4 = QtWidgets.QComboBox(self.countTab)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.label_19 = QtWidgets.QLabel(self.countTab)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 2, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Count.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.countTab, icon1, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.settingTab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.setPushButton = QtWidgets.QPushButton(self.settingTab)
        self.setPushButton.setObjectName("setPushButton")
        self.horizontalLayout.addWidget(self.setPushButton)
        self.clearPushButton = QtWidgets.QPushButton(self.settingTab)
        self.clearPushButton.setObjectName("clearPushButton")
        self.horizontalLayout.addWidget(self.clearPushButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.settingTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.settingTab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.settingTab)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lowRateLineEdit = QtWidgets.QLineEdit(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowRateLineEdit.sizePolicy().hasHeightForWidth())
        self.lowRateLineEdit.setSizePolicy(sizePolicy)
        self.lowRateLineEdit.setObjectName("lowRateLineEdit")
        self.gridLayout_4.addWidget(self.lowRateLineEdit, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_9.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.coldRadioButton = QtWidgets.QRadioButton(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coldRadioButton.sizePolicy().hasHeightForWidth())
        self.coldRadioButton.setSizePolicy(sizePolicy)
        self.coldRadioButton.setObjectName("coldRadioButton")
        self.gridLayout_4.addWidget(self.coldRadioButton, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)
        self.hotRadioButton = QtWidgets.QRadioButton(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hotRadioButton.sizePolicy().hasHeightForWidth())
        self.hotRadioButton.setSizePolicy(sizePolicy)
        self.hotRadioButton.setObjectName("hotRadioButton")
        self.gridLayout_4.addWidget(self.hotRadioButton, 0, 2, 1, 1)
        self.defaultTempLineEdit = QtWidgets.QLineEdit(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultTempLineEdit.sizePolicy().hasHeightForWidth())
        self.defaultTempLineEdit.setSizePolicy(sizePolicy)
        self.defaultTempLineEdit.setObjectName("defaultTempLineEdit")
        self.gridLayout_4.addWidget(self.defaultTempLineEdit, 3, 1, 1, 1)
        self.serviceNoComboBox = QtWidgets.QComboBox(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serviceNoComboBox.sizePolicy().hasHeightForWidth())
        self.serviceNoComboBox.setSizePolicy(sizePolicy)
        self.serviceNoComboBox.setObjectName("serviceNoComboBox")
        self.gridLayout_4.addWidget(self.serviceNoComboBox, 11, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 11, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 5, 0, 1, 1)
        self.lowTempLineEdit = QtWidgets.QLineEdit(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowTempLineEdit.sizePolicy().hasHeightForWidth())
        self.lowTempLineEdit.setSizePolicy(sizePolicy)
        self.lowTempLineEdit.setObjectName("lowTempLineEdit")
        self.gridLayout_4.addWidget(self.lowTempLineEdit, 1, 1, 1, 1)
        self.highTempLineEdit = QtWidgets.QLineEdit(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highTempLineEdit.sizePolicy().hasHeightForWidth())
        self.highTempLineEdit.setSizePolicy(sizePolicy)
        self.highTempLineEdit.setObjectName("highTempLineEdit")
        self.gridLayout_4.addWidget(self.highTempLineEdit, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.settingTab)
        self.label_3.setStyleSheet("qproperty-alignment:\'AlignCenter\'")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.defaultFanComboBox = QtWidgets.QComboBox(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultFanComboBox.sizePolicy().hasHeightForWidth())
        self.defaultFanComboBox.setSizePolicy(sizePolicy)
        self.defaultFanComboBox.setObjectName("defaultFanComboBox")
        self.gridLayout_4.addWidget(self.defaultFanComboBox, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 5, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 10, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.settingTab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.settingTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 8, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.settingTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)
        self.midRateLineEdit = QtWidgets.QLineEdit(self.settingTab)
        self.midRateLineEdit.setObjectName("midRateLineEdit")
        self.gridLayout_4.addWidget(self.midRateLineEdit, 6, 1, 1, 1)
        self.highRateLineEdit = QtWidgets.QLineEdit(self.settingTab)
        self.highRateLineEdit.setObjectName("highRateLineEdit")
        self.gridLayout_4.addWidget(self.highRateLineEdit, 7, 1, 1, 1)
        self.lowPLlineEdit = QtWidgets.QLineEdit(self.settingTab)
        self.lowPLlineEdit.setObjectName("lowPLlineEdit")
        self.gridLayout_4.addWidget(self.lowPLlineEdit, 8, 1, 1, 1)
        self.midPineEdit = QtWidgets.QLineEdit(self.settingTab)
        self.midPineEdit.setObjectName("midPineEdit")
        self.gridLayout_4.addWidget(self.midPineEdit, 9, 1, 1, 1)
        self.highPLineEdit = QtWidgets.QLineEdit(self.settingTab)
        self.highPLineEdit.setObjectName("highPLineEdit")
        self.gridLayout_4.addWidget(self.highPLineEdit, 10, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.settingTab)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 6, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.settingTab)
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 7, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.settingTab)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 8, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.settingTab)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 9, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.settingTab)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 10, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.line_2 = QtWidgets.QFrame(self.settingTab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_7 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_5.addWidget(self.checkBox_7, 7, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 5, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 8, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 7, 0, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_5.addWidget(self.checkBox_1, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 4, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 6, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_5.addWidget(self.checkBox_5, 5, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 4, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_5.addWidget(self.checkBox_6, 6, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.settingTab)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_5.addWidget(self.checkBox_8, 8, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.settingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 0, 0, 1, 1)
        self.vipCheckBox_1 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_1.setObjectName("vipCheckBox_1")
        self.gridLayout_5.addWidget(self.vipCheckBox_1, 1, 2, 1, 1)
        self.vipCheckBox_2 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_2.setObjectName("vipCheckBox_2")
        self.gridLayout_5.addWidget(self.vipCheckBox_2, 2, 2, 1, 1)
        self.vipCheckBox_3 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_3.setObjectName("vipCheckBox_3")
        self.gridLayout_5.addWidget(self.vipCheckBox_3, 3, 2, 1, 1)
        self.vipCheckBox_4 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_4.setObjectName("vipCheckBox_4")
        self.gridLayout_5.addWidget(self.vipCheckBox_4, 4, 2, 1, 1)
        self.vipCheckBox_5 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_5.setObjectName("vipCheckBox_5")
        self.gridLayout_5.addWidget(self.vipCheckBox_5, 5, 2, 1, 1)
        self.vipCheckBox_6 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_6.setObjectName("vipCheckBox_6")
        self.gridLayout_5.addWidget(self.vipCheckBox_6, 6, 2, 1, 1)
        self.vipCheckBox_7 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_7.setObjectName("vipCheckBox_7")
        self.gridLayout_5.addWidget(self.vipCheckBox_7, 7, 2, 1, 1)
        self.vipCheckBox_8 = QtWidgets.QCheckBox(self.settingTab)
        self.vipCheckBox_8.setObjectName("vipCheckBox_8")
        self.gridLayout_5.addWidget(self.vipCheckBox_8, 8, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_5)
        self.gridLayout_7.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem13, 1, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.settingTab, icon2, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serviceNoLabel.setText(_translate("MainWindow", "服务对象数"))
        self.label.setText(_translate("MainWindow", "默认风速"))
        self.rangeLabel.setText(_translate("MainWindow", "温度范围"))
        self.defaultTempLabel.setText(_translate("MainWindow", "默认温度"))
        self.modeLabel.setText(_translate("MainWindow", "工作模式"))
        item = self.detailtableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "房间号"))
        item = self.detailtableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "类型"))
        item = self.detailtableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "状态"))
        item = self.detailtableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "目标温度"))
        item = self.detailtableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "当前温度"))
        item = self.detailtableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "目标风速"))
        item = self.detailtableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "当前风速"))
        item = self.detailtableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "能耗"))
        item = self.detailtableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "费用"))
        self.pushButton.setText(_translate("MainWindow", "生成统计报表"))
        self.label_13.setText(_translate("MainWindow", "年"))
        self.label_18.setText(_translate("MainWindow", "月"))
        self.label_19.setText(_translate("MainWindow", "日"))
        self.setPushButton.setText(_translate("MainWindow", "确定"))
        self.clearPushButton.setText(_translate("MainWindow", "重置"))
        self.label_5.setText(_translate("MainWindow", "°C"))
        self.label_10.setText(_translate("MainWindow", "中风功率"))
        self.label_8.setText(_translate("MainWindow", "最低温度"))
        self.label_28.setText(_translate("MainWindow", "最高温度"))
        self.label_9.setText(_translate("MainWindow", "温控模式"))
        self.coldRadioButton.setText(_translate("MainWindow", "制冷"))
        self.label_11.setText(_translate("MainWindow", "缺省温度"))
        self.hotRadioButton.setText(_translate("MainWindow", "制热"))
        self.label_16.setText(_translate("MainWindow", "°C"))
        self.label_14.setText(_translate("MainWindow", "服务对象数"))
        self.label_12.setText(_translate("MainWindow", "弱风费率"))
        self.label_3.setText(_translate("MainWindow", "默认风速"))
        self.label_17.setText(_translate("MainWindow", "RMB/min"))
        self.label_15.setText(_translate("MainWindow", "强风功率"))
        self.label_6.setText(_translate("MainWindow", "强风费率"))
        self.label_4.setText(_translate("MainWindow", "°C"))
        self.label_30.setText(_translate("MainWindow", "弱风功率"))
        self.label_7.setText(_translate("MainWindow", "中风费率"))
        self.label_31.setText(_translate("MainWindow", "RMB/min"))
        self.label_32.setText(_translate("MainWindow", "RMB/min"))
        self.label_33.setText(_translate("MainWindow", "kw"))
        self.label_34.setText(_translate("MainWindow", "kw"))
        self.label_35.setText(_translate("MainWindow", "kw"))
        self.checkBox_7.setText(_translate("MainWindow", "普通"))
        self.label_22.setText(_translate("MainWindow", "312A"))
        self.label_24.setText(_translate("MainWindow", "313A"))
        self.label_27.setText(_translate("MainWindow", "315A"))
        self.label_26.setText(_translate("MainWindow", "314A"))
        self.checkBox_1.setText(_translate("MainWindow", "普通"))
        self.label_21.setText(_translate("MainWindow", "311B"))
        self.label_20.setText(_translate("MainWindow", "311A"))
        self.checkBox_2.setText(_translate("MainWindow", "普通"))
        self.checkBox_3.setText(_translate("MainWindow", "普通"))
        self.label_23.setText(_translate("MainWindow", "312B"))
        self.label_25.setText(_translate("MainWindow", "313B"))
        self.checkBox_5.setText(_translate("MainWindow", "普通"))
        self.checkBox_4.setText(_translate("MainWindow", "普通"))
        self.checkBox_6.setText(_translate("MainWindow", "普通"))
        self.checkBox_8.setText(_translate("MainWindow", "普通"))
        self.label_29.setText(_translate("MainWindow", "房间号"))
        self.vipCheckBox_1.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_2.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_3.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_4.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_5.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_6.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_7.setText(_translate("MainWindow", "VIP"))
        self.vipCheckBox_8.setText(_translate("MainWindow", "VIP"))

import qt
